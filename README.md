# config-generator
Generator to build config files in the style of classes for different languages.

## Currently supported languages
- [x] TypeScript
- [x] Java

## Usage
config-generator can either be used via the commandline or called from within Python and depends on the configuration passed to it.

### Commandline
```bash
python3 -m config-generator -c example/test-config.yaml -o example
```

## Configuration
For details about the configuration file, please check *example/test-config.yaml*. All possible values are described there. Basically the configuration consists of a *languages*- and a *properties*-section. The first one describes language specific properties e.g. for which language to generate, which naming convention to use for the output file or how much indent to use. The *properties*-section defines the actual values whereis the following types are supported: *bool*, *int*, *float*, *double*, *string* and *regex*. Properties can also act as helpers for other properties which don't need to be written to the final config-file. These properties can be marked as *hidden*. Acting as a helper-property means that it defines a value which other properties can use as substitute values referencing them via *${property-name}*.

### Example

```yaml
languages:
  - type: java                        # Specifies the output language. Supported values are: java | typescript
    file_naming: pascal               # Specifies the file naming convention. Supported values: snake | screaming_snake | camel | pascal | kebap
    indent: 4                         # Specifies the amount of spaces before each constant.
    package: my.test.package          # For Java, a package name must be specified.

  - type: typescript
    file_naming: kebap
    indent: 4

properties:
  - type: bool                        # Specifies the constant data type. Supported values: bool | int | float | double | string | regex
    name: myBoolean                   # Specifies the constant's name.
    value: true                       # Specifies the constant's value.

  - type: int
    name: myInteger
    value: 142

  - type: float
    name: myFloat
    value: 322f                       # Float with float specifier. However, an additional specifier (f) is not required and will be trimmed.

  - type: double
    name: myDouble
    value: 233.9

  - type: string
    name: myString
    value: Hello World
    hidden: true                      # If a property should act as a helper but should not be written to the generated file, it must be marked as 'hidden'.

  - type: regex
    name: myRegex
    value: Test Reg(E|e)x
    comment: Just another RegEx.      # Variables can be described using the comment property.

  - type: string
    name: mySubstitutedString
    value: Sometimes I just want to scream ${myString}!
```

```java
package my.test.package;

public class TestConfig {
    public final static boolean myBoolean = true;
    public final static int myInteger = 142;
    public final static float myFloat = 322.0f;
    public final static double myDouble = 233.9d;
    public final static String myRegex = "Test Reg(E|e)x"; /* Just another RegEx. */
    public final static String mySubstitutedString = "Sometimes I just want to scream Hello World!";
}

```

```typescript
export class TestConfig {
    public static readonly myBoolean = true;
    public static readonly myInteger = 142;
    public static readonly myFloat = 322.0;
    public static readonly myDouble = 233.9;
    public static readonly myRegex = /Test Reg(E|e)x/; /* Just another RegEx. */
    public static readonly mySubstitutedString = 'Sometimes I just want to scream Hello World!';
}
```
