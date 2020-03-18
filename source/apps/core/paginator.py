import logging

from django.core.paginator import Paginator
from django.utils.functional import cached_property

logger = logging.getLogger(__name__)


class FasterDjangoPaginator(Paginator):
    @cached_property
    def count(self):
        # only select 'id' for counting, much cheaper
        return self.object_list.values('id').count()
