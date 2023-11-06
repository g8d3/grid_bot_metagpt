## views.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from grid_bot_manager.models import User, Bot, db
from grid_bot_manager.forms import LoginForm, RegistrationForm, BotCreationForm
from grid_bot_manager.services.grid_bot_service import GridBotService

bot_blueprint = Blueprint('bot', __name__)

@bot_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@bot_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@bot_blueprint.route('/bot', methods=['GET', 'POST'])
@login_required
def create_bot():
    form = BotCreationForm()
    if form.validate_on_submit():
        bot = Bot(exchange=form.exchange.data, symbol=form.symbol.data, lower_price=form.lower_price.data, upper_price=form.upper_price.data, grid_levels=form.grid_levels.data, user=current_user)
        db.session.add(bot)
        db.session.commit()
        GridBotService.start_bot(bot)
        flash('Bot created successfully!')
        return redirect(url_for('index'))
    return render_template('create_bot.html', title='Create Bot', form=form)

@bot_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@bot_blueprint.route('/')
@bot_blueprint.route('/index')
@login_required
def index():
    bots = current_user.bots.all()
    return render_template('index.html', title='Home', bots=bots)
