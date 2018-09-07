# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)


from .resource_mapping import RESOURCE_MAPPING


class TheMoviedbClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://api.themoviedb.org/3/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(TheMoviedbClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)
        params.setdefault('params', {}).update(
            {'api_key': api_params.get('api_key', '')}
        )
        return params

    def get_iterator_list(self, response_data):
        return response_data['results']

    def get_iterator_next_request_kwargs(self, iterator_request_kwargs,
                                         response_data, response):
        pass


TheMovieDB = generate_wrapper_from_adapter(TheMoviedbClientAdapter)
