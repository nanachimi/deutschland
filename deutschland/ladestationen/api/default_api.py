"""
    Bundesnetzagentur: Ladesäulenregister

    API des Ladesäulenregisters der Bundesnetzagentur  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from deutschland.ladestationen.api_client import ApiClient, Endpoint as _Endpoint
from deutschland.ladestationen.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from deutschland.ladestationen.model.station_overview import StationOverview


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.query_get_endpoint = _Endpoint(
            settings={
                "response_type": (StationOverview,),
                "auth": [],
                "endpoint_path": "/query",
                "operation_id": "query_get",
                "http_method": "GET",
                "servers": [
                    {
                        "url": "https://services6.arcgis.com/6jU7RmJig2Wwo1b0/ArcGIS/rest/services/Ladesaeulenregister/FeatureServer/7",
                        "description": "No description provided",
                    },
                ],
            },
            params_map={
                "all": [
                    "geometry",
                    "out_fields",
                    "geometry_type",
                    "f",
                    "object_ids",
                    "order_by_fields",
                    "return_geometry",
                    "spatial_rel",
                    "in_sr",
                    "out_sr",
                    "max_record_count_factor",
                    "result_type",
                    "quantization_parameters",
                    "where",
                    "having",
                    "time",
                    "distance",
                    "units",
                    "geometry_precision",
                    "feature_encoding",
                    "group_by_fields_for_statistics",
                    "cache_hint",
                    "return_extent_only",
                    "return_z",
                    "return_ids_only",
                    "return_centroid",
                    "return_exceeded_limit_features",
                    "datum_transformation",
                    "result_offset",
                    "apply_vcs_projection",
                    "out_statistics",
                    "return_distinct_values",
                    "multipatch_option",
                    "return_m",
                    "max_allowable_offset",
                    "return_count_only",
                    "return_unique_ids_only",
                    "return_query_geometry",
                    "result_record_count",
                    "sql_format",
                    "token",
                    "return_geodetic",
                ],
                "required": [
                    "geometry",
                    "out_fields",
                ],
                "nullable": [],
                "enum": [
                    "geometry_type",
                    "f",
                    "spatial_rel",
                    "result_type",
                    "units",
                    "feature_encoding",
                    "multipatch_option",
                    "sql_format",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("geometry_type",): {
                        "ESRIGEOMETRYENVELOPE": "esriGeometryEnvelope",
                        "ESRIGEOMETRYPOINT": "esriGeometryPoint",
                        "ESRIGEOMETRYPOLYLINE": "esriGeometryPolyline",
                        "ESRIGEOMETRYPOLYGON": "esriGeometryPolygon",
                        "ESRIGEOMETRYMULTIPOINT": "esriGeometryMultipoint",
                    },
                    ("f",): {
                        "JSON": "json",
                        "GEOJSON": "geojson",
                        "PBF": "pbf",
                        "HTML": "html",
                    },
                    ("spatial_rel",): {
                        "ESRISPATIALRELINTERSECTS": "esriSpatialRelIntersects",
                        "ESRISPATIALRELCONTAINS": "esriSpatialRelContains",
                        "ESRISPATIALRELCROSSES": "esriSpatialRelCrosses",
                        "ESRISPATIALRELENVELOPEINTERSECTS": "esriSpatialRelEnvelopeIntersects",
                        "ESRISPATIALRELINDEXINTERSECTS": "esriSpatialRelIndexIntersects",
                        "ESRISPATIALRELOVERLAPS": "esriSpatialRelOverlaps",
                        "ESRISPATIALRELTOUCHES": "esriSpatialRelTouches",
                        "ESRISPATIALRELWITHIN": "esriSpatialRelWithin",
                        "ESRISPATIALRELDISJOINT": "esriSpatialRelDisjoint",
                    },
                    ("result_type",): {
                        "NONE": "none",
                        "STANDARD": "standard",
                        "TILE": "tile",
                    },
                    ("units",): {
                        "METER": "esriSRUnit_Meter",
                        "STATUTEMILE": "esriSRUnit_StatuteMile",
                        "FOOT": "esriSRUnit_Foot",
                        "KILOMETER": "esriSRUnit_Kilometer",
                        "NAUTICALMILE": "esriSRUnit_NauticalMile",
                        "USNAUTICALMILE": "esriSRUnit_USNauticalMile",
                    },
                    ("feature_encoding",): {
                        "ESRIDEFAULT": "esriDefault",
                        "ESRICOMPRESSEDSHAPEBUFFER": "esriCompressedShapeBuffer",
                    },
                    ("multipatch_option",): {
                        "NONE": "none",
                        "XYFOOTPRINT": "xyFootprint",
                        "STRIPMATERIALS": "stripMaterials",
                        "EMBEDMATERIALS": "embedMaterials",
                        "EXTERNALIZETEXTURES": "externalizeTextures",
                        "EXTENT": "extent",
                    },
                    ("sql_format",): {
                        "NONE": "none",
                        "STANDARD": "standard",
                        "NATIVE": "native",
                    },
                },
                "openapi_types": {
                    "geometry": (str,),
                    "out_fields": (str,),
                    "geometry_type": (str,),
                    "f": (str,),
                    "object_ids": (str,),
                    "order_by_fields": (str,),
                    "return_geometry": (bool,),
                    "spatial_rel": (str,),
                    "in_sr": (int,),
                    "out_sr": (int,),
                    "max_record_count_factor": (int,),
                    "result_type": (str,),
                    "quantization_parameters": (str,),
                    "where": (str,),
                    "having": (str,),
                    "time": (int,),
                    "distance": (str,),
                    "units": (str,),
                    "geometry_precision": (str,),
                    "feature_encoding": (str,),
                    "group_by_fields_for_statistics": (str,),
                    "cache_hint": (bool,),
                    "return_extent_only": (bool,),
                    "return_z": (bool,),
                    "return_ids_only": (bool,),
                    "return_centroid": (bool,),
                    "return_exceeded_limit_features": (bool,),
                    "datum_transformation": (str,),
                    "result_offset": (str,),
                    "apply_vcs_projection": (bool,),
                    "out_statistics": (str,),
                    "return_distinct_values": (bool,),
                    "multipatch_option": (str,),
                    "return_m": (bool,),
                    "max_allowable_offset": (int,),
                    "return_count_only": (bool,),
                    "return_unique_ids_only": (bool,),
                    "return_query_geometry": (bool,),
                    "result_record_count": (int,),
                    "sql_format": (str,),
                    "token": (str,),
                    "return_geodetic": (bool,),
                },
                "attribute_map": {
                    "geometry": "geometry",
                    "out_fields": "outFields",
                    "geometry_type": "geometryType",
                    "f": "f",
                    "object_ids": "objectIds",
                    "order_by_fields": "orderByFields",
                    "return_geometry": "returnGeometry",
                    "spatial_rel": "spatialRel",
                    "in_sr": "inSR",
                    "out_sr": "outSR",
                    "max_record_count_factor": "maxRecordCountFactor",
                    "result_type": "resultType",
                    "quantization_parameters": "quantizationParameters",
                    "where": "where",
                    "having": "having",
                    "time": "time",
                    "distance": "distance",
                    "units": "units",
                    "geometry_precision": "geometryPrecision",
                    "feature_encoding": "featureEncoding",
                    "group_by_fields_for_statistics": "groupByFieldsForStatistics",
                    "cache_hint": "cacheHint",
                    "return_extent_only": "returnExtentOnly",
                    "return_z": "returnZ",
                    "return_ids_only": "returnIdsOnly",
                    "return_centroid": "returnCentroid",
                    "return_exceeded_limit_features": "returnExceededLimitFeatures",
                    "datum_transformation": "datumTransformation",
                    "result_offset": "resultOffset",
                    "apply_vcs_projection": "applyVCSProjection",
                    "out_statistics": "outStatistics",
                    "return_distinct_values": "returnDistinctValues",
                    "multipatch_option": "multipatchOption",
                    "return_m": "returnM",
                    "max_allowable_offset": "maxAllowableOffset",
                    "return_count_only": "returnCountOnly",
                    "return_unique_ids_only": "returnUniqueIdsOnly",
                    "return_query_geometry": "returnQueryGeometry",
                    "result_record_count": "resultRecordCount",
                    "sql_format": "sqlFormat",
                    "token": "token",
                    "return_geodetic": "returnGeodetic",
                },
                "location_map": {
                    "geometry": "query",
                    "out_fields": "query",
                    "geometry_type": "query",
                    "f": "query",
                    "object_ids": "query",
                    "order_by_fields": "query",
                    "return_geometry": "query",
                    "spatial_rel": "query",
                    "in_sr": "query",
                    "out_sr": "query",
                    "max_record_count_factor": "query",
                    "result_type": "query",
                    "quantization_parameters": "query",
                    "where": "query",
                    "having": "query",
                    "time": "query",
                    "distance": "query",
                    "units": "query",
                    "geometry_precision": "query",
                    "feature_encoding": "query",
                    "group_by_fields_for_statistics": "query",
                    "cache_hint": "query",
                    "return_extent_only": "query",
                    "return_z": "query",
                    "return_ids_only": "query",
                    "return_centroid": "query",
                    "return_exceeded_limit_features": "query",
                    "datum_transformation": "query",
                    "result_offset": "query",
                    "apply_vcs_projection": "query",
                    "out_statistics": "query",
                    "return_distinct_values": "query",
                    "multipatch_option": "query",
                    "return_m": "query",
                    "max_allowable_offset": "query",
                    "return_count_only": "query",
                    "return_unique_ids_only": "query",
                    "return_query_geometry": "query",
                    "result_record_count": "query",
                    "sql_format": "query",
                    "token": "query",
                    "return_geodetic": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def query_get(self, geometry, out_fields="*", **kwargs):
        """Query für alle Ladesäulen  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.query_get(geometry, out_fields="*", async_req=True)
        >>> result = thread.get()

        Args:
            geometry (str): Geometry filter. URL-enkodiertes JSON Objekt vom Typ `Geometry`
            out_fields (str): Auswahl der Felder, die ausgegeben werden sollen, durch Komma getrennt. defaults to "*", must be one of ["*"]

        Keyword Args:
            geometry_type (str): Art der Geometry. [optional] if omitted the server will use the default value of ""
            f (str): Ausgabeformat der Daten. Default ist 'html'.. [optional]
            object_ids (str): Komma-separierte Liste von IDs (integer), filtert nach den einzelnen Objekten. [optional]
            order_by_fields (str): [optional]
            return_geometry (bool): [optional]
            spatial_rel (str): Spatial Relationships. [optional]
            in_sr (int): Input Spatial Reference. [optional]
            out_sr (int): Output Spatial Reference. [optional]
            max_record_count_factor (int): [optional]
            result_type (str): [optional]
            quantization_parameters (str): URL-enkodiertes JSON Objekt vom Typ `QuantizationParameter`. [optional]
            where (str): SQL \"where\" Filter. [optional]
            having (str): [optional]
            time (int): [optional]
            distance (str): [optional]
            units (str): [optional]
            geometry_precision (str): [optional]
            feature_encoding (str): [optional]
            group_by_fields_for_statistics (str): [optional]
            cache_hint (bool): [optional]
            return_extent_only (bool): [optional]
            return_z (bool): [optional]
            return_ids_only (bool): [optional]
            return_centroid (bool): [optional]
            return_exceeded_limit_features (bool): [optional]
            datum_transformation (str): [optional]
            result_offset (str): [optional]
            apply_vcs_projection (bool): [optional]
            out_statistics (str): [optional]
            return_distinct_values (bool): [optional]
            multipatch_option (str): [optional]
            return_m (bool): [optional]
            max_allowable_offset (int): [optional]
            return_count_only (bool): [optional]
            return_unique_ids_only (bool): [optional]
            return_query_geometry (bool): [optional]
            result_record_count (int): [optional]
            sql_format (str): [optional]
            token (str): [optional]
            return_geodetic (bool): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            StationOverview
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["geometry"] = geometry
        kwargs["out_fields"] = out_fields
        return self.query_get_endpoint.call_with_http_info(**kwargs)
