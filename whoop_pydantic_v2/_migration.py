import sys
from typing import Any, Callable, Dict

from .version import version_short

MOVED_IN_V2 = {
    'whoop_pydantic_v2.utils:version_info': 'whoop_pydantic_v2.version:version_info',
    'whoop_pydantic_v2.error_wrappers:ValidationError': 'whoop_pydantic_v2:ValidationError',
    'whoop_pydantic_v2.utils:to_camel': 'whoop_pydantic_v2.alias_generators:to_pascal',
    'whoop_pydantic_v2.utils:to_lower_camel': 'whoop_pydantic_v2.alias_generators:to_camel',
    'whoop_pydantic_v2:PyObject': 'whoop_pydantic_v2.types:ImportString',
    'whoop_pydantic_v2.types:PyObject': 'whoop_pydantic_v2.types:ImportString',
    'whoop_pydantic_v2.generics:GenericModel': 'whoop_pydantic_v2.BaseModel',
}

DEPRECATED_MOVED_IN_V2 = {
    'whoop_pydantic_v2.tools:schema_of': 'whoop_pydantic_v2.deprecated.tools:schema_of',
    'whoop_pydantic_v2.tools:parse_obj_as': 'whoop_pydantic_v2.deprecated.tools:parse_obj_as',
    'whoop_pydantic_v2.tools:schema_json_of': 'whoop_pydantic_v2.deprecated.tools:schema_json_of',
    'whoop_pydantic_v2.json:pydantic_encoder': 'whoop_pydantic_v2.deprecated.json:pydantic_encoder',
    'whoop_pydantic_v2:validate_arguments': 'whoop_pydantic_v2.deprecated.decorator:validate_arguments',
    'whoop_pydantic_v2.json:custom_pydantic_encoder': 'whoop_pydantic_v2.deprecated.json:custom_pydantic_encoder',
    'whoop_pydantic_v2.json:timedelta_isoformat': 'whoop_pydantic_v2.deprecated.json:timedelta_isoformat',
    'whoop_pydantic_v2.decorator:validate_arguments': 'whoop_pydantic_v2.deprecated.decorator:validate_arguments',
    'whoop_pydantic_v2.class_validators:validator': 'whoop_pydantic_v2.deprecated.class_validators:validator',
    'whoop_pydantic_v2.class_validators:root_validator': 'whoop_pydantic_v2.deprecated.class_validators:root_validator',
    'whoop_pydantic_v2.config:BaseConfig': 'whoop_pydantic_v2.deprecated.config:BaseConfig',
    'whoop_pydantic_v2.config:Extra': 'whoop_pydantic_v2.deprecated.config:Extra',
}

REDIRECT_TO_V1 = {
    f'whoop_pydantic_v2.utils:{obj}': f'whoop_pydantic_v2.v1.utils:{obj}'
    for obj in (
        'deep_update',
        'GetterDict',
        'lenient_issubclass',
        'lenient_isinstance',
        'is_valid_field',
        'update_not_none',
        'import_string',
        'Representation',
        'ROOT_KEY',
        'smart_deepcopy',
        'sequence_like',
    )
}


REMOVED_IN_V2 = {
    'whoop_pydantic_v2:ConstrainedBytes',
    'whoop_pydantic_v2:ConstrainedDate',
    'whoop_pydantic_v2:ConstrainedDecimal',
    'whoop_pydantic_v2:ConstrainedFloat',
    'whoop_pydantic_v2:ConstrainedFrozenSet',
    'whoop_pydantic_v2:ConstrainedInt',
    'whoop_pydantic_v2:ConstrainedList',
    'whoop_pydantic_v2:ConstrainedSet',
    'whoop_pydantic_v2:ConstrainedStr',
    'whoop_pydantic_v2:JsonWrapper',
    'whoop_pydantic_v2:NoneBytes',
    'whoop_pydantic_v2:NoneStr',
    'whoop_pydantic_v2:NoneStrBytes',
    'whoop_pydantic_v2:Protocol',
    'whoop_pydantic_v2:Required',
    'whoop_pydantic_v2:StrBytes',
    'whoop_pydantic_v2:compiled',
    'whoop_pydantic_v2.config:get_config',
    'whoop_pydantic_v2.config:inherit_config',
    'whoop_pydantic_v2.config:prepare_config',
    'whoop_pydantic_v2:create_model_from_namedtuple',
    'whoop_pydantic_v2:create_model_from_typeddict',
    'whoop_pydantic_v2.dataclasses:create_pydantic_model_from_dataclass',
    'whoop_pydantic_v2.dataclasses:make_dataclass_validator',
    'whoop_pydantic_v2.dataclasses:set_validation',
    'whoop_pydantic_v2.datetime_parse:parse_date',
    'whoop_pydantic_v2.datetime_parse:parse_time',
    'whoop_pydantic_v2.datetime_parse:parse_datetime',
    'whoop_pydantic_v2.datetime_parse:parse_duration',
    'whoop_pydantic_v2.error_wrappers:ErrorWrapper',
    'whoop_pydantic_v2.errors:AnyStrMaxLengthError',
    'whoop_pydantic_v2.errors:AnyStrMinLengthError',
    'whoop_pydantic_v2.errors:ArbitraryTypeError',
    'whoop_pydantic_v2.errors:BoolError',
    'whoop_pydantic_v2.errors:BytesError',
    'whoop_pydantic_v2.errors:CallableError',
    'whoop_pydantic_v2.errors:ClassError',
    'whoop_pydantic_v2.errors:ColorError',
    'whoop_pydantic_v2.errors:ConfigError',
    'whoop_pydantic_v2.errors:DataclassTypeError',
    'whoop_pydantic_v2.errors:DateError',
    'whoop_pydantic_v2.errors:DateNotInTheFutureError',
    'whoop_pydantic_v2.errors:DateNotInThePastError',
    'whoop_pydantic_v2.errors:DateTimeError',
    'whoop_pydantic_v2.errors:DecimalError',
    'whoop_pydantic_v2.errors:DecimalIsNotFiniteError',
    'whoop_pydantic_v2.errors:DecimalMaxDigitsError',
    'whoop_pydantic_v2.errors:DecimalMaxPlacesError',
    'whoop_pydantic_v2.errors:DecimalWholeDigitsError',
    'whoop_pydantic_v2.errors:DictError',
    'whoop_pydantic_v2.errors:DurationError',
    'whoop_pydantic_v2.errors:EmailError',
    'whoop_pydantic_v2.errors:EnumError',
    'whoop_pydantic_v2.errors:EnumMemberError',
    'whoop_pydantic_v2.errors:ExtraError',
    'whoop_pydantic_v2.errors:FloatError',
    'whoop_pydantic_v2.errors:FrozenSetError',
    'whoop_pydantic_v2.errors:FrozenSetMaxLengthError',
    'whoop_pydantic_v2.errors:FrozenSetMinLengthError',
    'whoop_pydantic_v2.errors:HashableError',
    'whoop_pydantic_v2.errors:IPv4AddressError',
    'whoop_pydantic_v2.errors:IPv4InterfaceError',
    'whoop_pydantic_v2.errors:IPv4NetworkError',
    'whoop_pydantic_v2.errors:IPv6AddressError',
    'whoop_pydantic_v2.errors:IPv6InterfaceError',
    'whoop_pydantic_v2.errors:IPv6NetworkError',
    'whoop_pydantic_v2.errors:IPvAnyAddressError',
    'whoop_pydantic_v2.errors:IPvAnyInterfaceError',
    'whoop_pydantic_v2.errors:IPvAnyNetworkError',
    'whoop_pydantic_v2.errors:IntEnumError',
    'whoop_pydantic_v2.errors:IntegerError',
    'whoop_pydantic_v2.errors:InvalidByteSize',
    'whoop_pydantic_v2.errors:InvalidByteSizeUnit',
    'whoop_pydantic_v2.errors:InvalidDiscriminator',
    'whoop_pydantic_v2.errors:InvalidLengthForBrand',
    'whoop_pydantic_v2.errors:JsonError',
    'whoop_pydantic_v2.errors:JsonTypeError',
    'whoop_pydantic_v2.errors:ListError',
    'whoop_pydantic_v2.errors:ListMaxLengthError',
    'whoop_pydantic_v2.errors:ListMinLengthError',
    'whoop_pydantic_v2.errors:ListUniqueItemsError',
    'whoop_pydantic_v2.errors:LuhnValidationError',
    'whoop_pydantic_v2.errors:MissingDiscriminator',
    'whoop_pydantic_v2.errors:MissingError',
    'whoop_pydantic_v2.errors:NoneIsAllowedError',
    'whoop_pydantic_v2.errors:NoneIsNotAllowedError',
    'whoop_pydantic_v2.errors:NotDigitError',
    'whoop_pydantic_v2.errors:NotNoneError',
    'whoop_pydantic_v2.errors:NumberNotGeError',
    'whoop_pydantic_v2.errors:NumberNotGtError',
    'whoop_pydantic_v2.errors:NumberNotLeError',
    'whoop_pydantic_v2.errors:NumberNotLtError',
    'whoop_pydantic_v2.errors:NumberNotMultipleError',
    'whoop_pydantic_v2.errors:PathError',
    'whoop_pydantic_v2.errors:PathNotADirectoryError',
    'whoop_pydantic_v2.errors:PathNotAFileError',
    'whoop_pydantic_v2.errors:PathNotExistsError',
    'whoop_pydantic_v2.errors:PatternError',
    'whoop_pydantic_v2.errors:PyObjectError',
    'whoop_pydantic_v2.errors:PydanticTypeError',
    'whoop_pydantic_v2.errors:PydanticValueError',
    'whoop_pydantic_v2.errors:SequenceError',
    'whoop_pydantic_v2.errors:SetError',
    'whoop_pydantic_v2.errors:SetMaxLengthError',
    'whoop_pydantic_v2.errors:SetMinLengthError',
    'whoop_pydantic_v2.errors:StrError',
    'whoop_pydantic_v2.errors:StrRegexError',
    'whoop_pydantic_v2.errors:StrictBoolError',
    'whoop_pydantic_v2.errors:SubclassError',
    'whoop_pydantic_v2.errors:TimeError',
    'whoop_pydantic_v2.errors:TupleError',
    'whoop_pydantic_v2.errors:TupleLengthError',
    'whoop_pydantic_v2.errors:UUIDError',
    'whoop_pydantic_v2.errors:UUIDVersionError',
    'whoop_pydantic_v2.errors:UrlError',
    'whoop_pydantic_v2.errors:UrlExtraError',
    'whoop_pydantic_v2.errors:UrlHostError',
    'whoop_pydantic_v2.errors:UrlHostTldError',
    'whoop_pydantic_v2.errors:UrlPortError',
    'whoop_pydantic_v2.errors:UrlSchemeError',
    'whoop_pydantic_v2.errors:UrlSchemePermittedError',
    'whoop_pydantic_v2.errors:UrlUserInfoError',
    'whoop_pydantic_v2.errors:WrongConstantError',
    'whoop_pydantic_v2.main:validate_model',
    'whoop_pydantic_v2.networks:stricturl',
    'whoop_pydantic_v2:parse_file_as',
    'whoop_pydantic_v2:parse_raw_as',
    'whoop_pydantic_v2:stricturl',
    'whoop_pydantic_v2.tools:parse_file_as',
    'whoop_pydantic_v2.tools:parse_raw_as',
    'whoop_pydantic_v2.types:ConstrainedBytes',
    'whoop_pydantic_v2.types:ConstrainedDate',
    'whoop_pydantic_v2.types:ConstrainedDecimal',
    'whoop_pydantic_v2.types:ConstrainedFloat',
    'whoop_pydantic_v2.types:ConstrainedFrozenSet',
    'whoop_pydantic_v2.types:ConstrainedInt',
    'whoop_pydantic_v2.types:ConstrainedList',
    'whoop_pydantic_v2.types:ConstrainedSet',
    'whoop_pydantic_v2.types:ConstrainedStr',
    'whoop_pydantic_v2.types:JsonWrapper',
    'whoop_pydantic_v2.types:NoneBytes',
    'whoop_pydantic_v2.types:NoneStr',
    'whoop_pydantic_v2.types:NoneStrBytes',
    'whoop_pydantic_v2.types:StrBytes',
    'whoop_pydantic_v2.typing:evaluate_forwardref',
    'whoop_pydantic_v2.typing:AbstractSetIntStr',
    'whoop_pydantic_v2.typing:AnyCallable',
    'whoop_pydantic_v2.typing:AnyClassMethod',
    'whoop_pydantic_v2.typing:CallableGenerator',
    'whoop_pydantic_v2.typing:DictAny',
    'whoop_pydantic_v2.typing:DictIntStrAny',
    'whoop_pydantic_v2.typing:DictStrAny',
    'whoop_pydantic_v2.typing:IntStr',
    'whoop_pydantic_v2.typing:ListStr',
    'whoop_pydantic_v2.typing:MappingIntStrAny',
    'whoop_pydantic_v2.typing:NoArgAnyCallable',
    'whoop_pydantic_v2.typing:NoneType',
    'whoop_pydantic_v2.typing:ReprArgs',
    'whoop_pydantic_v2.typing:SetStr',
    'whoop_pydantic_v2.typing:StrPath',
    'whoop_pydantic_v2.typing:TupleGenerator',
    'whoop_pydantic_v2.typing:WithArgsTypes',
    'whoop_pydantic_v2.typing:all_literal_values',
    'whoop_pydantic_v2.typing:display_as_type',
    'whoop_pydantic_v2.typing:get_all_type_hints',
    'whoop_pydantic_v2.typing:get_args',
    'whoop_pydantic_v2.typing:get_origin',
    'whoop_pydantic_v2.typing:get_sub_types',
    'whoop_pydantic_v2.typing:is_callable_type',
    'whoop_pydantic_v2.typing:is_classvar',
    'whoop_pydantic_v2.typing:is_finalvar',
    'whoop_pydantic_v2.typing:is_literal_type',
    'whoop_pydantic_v2.typing:is_namedtuple',
    'whoop_pydantic_v2.typing:is_new_type',
    'whoop_pydantic_v2.typing:is_none_type',
    'whoop_pydantic_v2.typing:is_typeddict',
    'whoop_pydantic_v2.typing:is_typeddict_special',
    'whoop_pydantic_v2.typing:is_union',
    'whoop_pydantic_v2.typing:new_type_supertype',
    'whoop_pydantic_v2.typing:resolve_annotations',
    'whoop_pydantic_v2.typing:typing_base',
    'whoop_pydantic_v2.typing:update_field_forward_refs',
    'whoop_pydantic_v2.typing:update_model_forward_refs',
    'whoop_pydantic_v2.utils:ClassAttribute',
    'whoop_pydantic_v2.utils:DUNDER_ATTRIBUTES',
    'whoop_pydantic_v2.utils:PyObjectStr',
    'whoop_pydantic_v2.utils:ValueItems',
    'whoop_pydantic_v2.utils:almost_equal_floats',
    'whoop_pydantic_v2.utils:get_discriminator_alias_and_values',
    'whoop_pydantic_v2.utils:get_model',
    'whoop_pydantic_v2.utils:get_unique_discriminator_alias',
    'whoop_pydantic_v2.utils:in_ipython',
    'whoop_pydantic_v2.utils:is_valid_identifier',
    'whoop_pydantic_v2.utils:path_type',
    'whoop_pydantic_v2.utils:validate_field_name',
    'whoop_pydantic_v2:validate_model',
}


def getattr_migration(module: str) -> Callable[[str], Any]:
    """Implement PEP 562 for objects that were either moved or removed on the migration
    to V2.

    Args:
        module: The module name.

    Returns:
        A callable that will raise an error if the object is not found.
    """
    # This avoids circular import with errors.py.
    from .errors import PydanticImportError

    def wrapper(name: str) -> object:
        """Raise an error if the object is not found, or warn if it was moved.

        In case it was moved, it still returns the object.

        Args:
            name: The object name.

        Returns:
            The object.
        """
        if name == '__path__':
            raise AttributeError(f'module {module!r} has no attribute {name!r}')

        import warnings

        from ._internal._validators import import_string

        import_path = f'{module}:{name}'
        if import_path in MOVED_IN_V2.keys():
            new_location = MOVED_IN_V2[import_path]
            warnings.warn(f'`{import_path}` has been moved to `{new_location}`.')
            return import_string(MOVED_IN_V2[import_path])
        if import_path in DEPRECATED_MOVED_IN_V2:
            # skip the warning here because a deprecation warning will be raised elsewhere
            return import_string(DEPRECATED_MOVED_IN_V2[import_path])
        if import_path in REDIRECT_TO_V1:
            new_location = REDIRECT_TO_V1[import_path]
            warnings.warn(
                f'`{import_path}` has been removed. We are importing from `{new_location}` instead.'
                'See the migration guide for more details: https://docs.pydantic.dev/latest/migration/'
            )
            return import_string(REDIRECT_TO_V1[import_path])
        if import_path == 'whoop_pydantic_v2:BaseSettings':
            raise PydanticImportError(
                '`BaseSettings` has been moved to the `whoop_pydantic_v2-settings` package. '
                f'See https://docs.pydantic.dev/{version_short()}/migration/#basesettings-has-moved-to-whoop_pydantic_v2-settings '
                'for more details.'
            )
        if import_path in REMOVED_IN_V2:
            raise PydanticImportError(f'`{import_path}` has been removed in V2.')
        globals: Dict[str, Any] = sys.modules[module].__dict__
        if name in globals:
            return globals[name]
        raise AttributeError(f'module {module!r} has no attribute {name!r}')

    return wrapper
