
from django.db.models import Q
import datetime

from api.models import User, Agent, Event, Group


def get_active_users() -> User:
    """Traga todos os uarios ativos, seu último login deve ser menor que 10 dias """
    today = datetime.date.today()
    query_set = User.objects.filter(last_login__gte=(today - datetime.timedelta(10)))
    return query_set


def get_amount_users() -> User:
    """Retorne a quantidade total de usuarios do sistema """
    query_set = User.objects.count()
    return query_set


def get_admin_users() -> User:
    """Traga todos os usuarios com grupo = 'admin"""
    query_set = User.objects.filter(group__name='admin')
    return query_set


def get_all_debug_events() -> Event:
    """Traga todos os eventos com tipo debug"""
    query_set = Event.objects.filter(level='debug')
    return query_set


def get_all_critical_events_by_user(agent) -> Event:
    """Traga todos os eventos do tipo critico de um usuário específico"""
    query_set = Event.objects.filter(
        Q(level='critical') & Q(agent=agent)
    )
    return query_set


def get_all_agents_by_user(username) -> Agent:
    """Traga todos os agentes de associados a um usuário pelo nome do usuário"""
    query_set = Agent.objects.filter(user__name=username)
    return query_set


def get_all_events_by_group() -> Group:
    """Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information"""
    query_set = Group.objects.filter(
        user__agent__event__level='information'
    )
    return query_set
