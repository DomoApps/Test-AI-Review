---
stoplight-id: e04caa9abb5cc
---

# Domo SDKs

Domo officially supports both a Java and Python SDK that provide the quickest path to developing on top of Domo's APIs.

## Java
---
Visit the [Java SDK Repository](https://github.com/domoinc/domo-java-sdk) for full usage and examples.

The Java SDK is published to [Maven](https://mvnrepository.com/) and can be added to your project in three ways:

### Maven
```java
<dependency>
  <groupId>com.domo</groupId>
  <artifactId>domo-java-sdk</artifactId>
  <version>0.1.0</version>
</dependency>
```
### Gradle
```java
compile 'com.domo:domo-java-sdk:0.1.0'
```
### Classic Jar Import
- Clone the [Java SDK Repository](https://github.com/domoinc/domo-java-sdk)
- Using a Bash Terminal, navigate to the cloned repository folder
- Create the Jar files via the Bash command `./gradlew bootRepackage`
- The Jars will be located in `build/libs/`
- Copy the Jars to your project folder, and add them to your build path



## Python
---

Visit the [Python SDK Repository](https://github.com/domoinc/domo-python-sdk) for full usage and examples.

The Python SDK is published to [PyPI](https://pypi.python.org/pypi/pydomo), and can be installed via the Pip command:

```bash
pip3 install pydomo requests jsonpickle
```
Once installed, the SDK can be added to your project via:
```python
from pydomo import Domo
```
