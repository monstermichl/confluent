from typing import List

from ..helpers.package_handling import evaluate_package

from ..base.name_converter import NamingConventionType
from ..base.generator_naming_conventions import GeneratorNamingConventions
from ..base.generator_base import _DEFAULT_INDENT, GeneratorBase
from ..base.property import Property
from ..base.property_type import PropertyType


class JavaGenerator(GeneratorBase):
    """
    Java specific generator. For more information about the generator methods, refer to GeneratorBase.
    """

    def __init__(
        self,
        type_name: str,
        properties: List[Property] = [],
        indent: int = _DEFAULT_INDENT,
        naming_conventions: GeneratorNamingConventions = None,
        additional_props = {}
    ):
        super().__init__(type_name, properties, indent, naming_conventions, additional_props)

        # Evaluate the config's package name.
        self.package = evaluate_package(
            r'^[a-z][a-z0-9_]+(\.[a-z0-9_]+)*$',
            'See also https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html',
            **self._additional_props,
        )

    def _default_type_naming_convention(self) -> NamingConventionType:
        return NamingConventionType.PASCAL_CASE
    
    def _before_type(self) -> str:
        return f'package {self.package};\n\n'

    def _property_before_type(self, _: Property) -> str:
        return ''
    
    def _start_type(self, type_name: str) -> str:
        return f'public class {type_name} {{'

    def _property_in_type(self, property: Property) -> str:
        match property.type:
            case PropertyType.BOOL:
                type = 'boolean'
                value = 'true' if property.value else 'false'
            case PropertyType.INT:
                type = 'int'
                value = property.value
            case PropertyType.FLOAT:
                type = 'float'
                value = f'{property.value}f'
            case PropertyType.DOUBLE:
                type = 'double'
                value = f'{property.value}d'
            case PropertyType.STRING | PropertyType.REGEX:
                type = 'String'
                value = property.value.replace('\\', '\\\\')  # TODO: Might need to be refined.
                value = f'"{value}"'  # Wrap in quotes.
            case _:
                raise Exception('Unknown type')

        return f'public final static {type} {property.name} = {value};'
    
    def _property_comment(self, comment: str) -> str:
        return f' // {comment}'
    
    def _end_type(self) -> str:
        return '}'

    def _property_after_type(self, _: Property) -> str:
        return ''
    
    def _after_type(self) -> str:
        return ''
