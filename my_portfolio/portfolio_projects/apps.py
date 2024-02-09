from django.apps import AppConfig


class PortfolioProjectsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio_projects'

    def ready(self):
        import portfolio_projects.signals
