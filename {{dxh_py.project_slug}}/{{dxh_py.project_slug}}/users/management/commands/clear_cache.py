from django.core.management.base import BaseCommand
from {{dxh_py.project_slug}}.utils.cache import CacheManager

class Command(BaseCommand):
    help = "Manage Django Cache (Clear all, by key, or by prefix)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--all",
            action="store_true",
            help="Clear all cache",
        )
        parser.add_argument(
            "--key",
            type=str,
            help="Clear cache by specific key",
        )
        parser.add_argument(
            "--prefix",
            type=str,
            help="Clear cache by prefix",
        )

    def handle(self, *args, **options):
        if options["all"]:
            CacheManager.clear_all()
            self.stdout.write(self.style.SUCCESS("Successfully cleared all cache."))
        
        elif options["key"]:
            CacheManager.delete(options["key"])
            self.stdout.write(self.style.SUCCESS(f"Successfully cleared cache key: {options['key']}"))
            
        elif options["prefix"]:
            CacheManager.clear_by_prefix(options["prefix"])
            self.stdout.write(self.style.SUCCESS(f"Successfully cleared cache with prefix: {options['prefix']}"))
            
        else:
            self.stdout.write(self.style.WARNING("Please specify --all, --key, or --prefix"))
