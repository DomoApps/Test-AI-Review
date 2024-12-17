# Introduction to Code Engine

Today we'll be exploring Domo's Code Engine capabilities and complete multiple exercises to get a sense for how Code engine can unlock new functionality to drive action and automation in Domo.

**Objectives:**
Learn how to implement CodeEngine functions and build basic Workflows (we will be writing scripts against Domo APIs to facilitate automation)
Understand correct way to pass authentication in CodeEngine
 
**Target Audience:**
Developers / Engineers with JavaScript or Python exposure.


## Outline

1. High-level overview of code engine
2. Anatomy of a Code Engine Function
   - Review existing global functions
   - Resource: [Code Engine Library Functions](https://domo-support.domo.com/s/article/000005173?language=en_US#code_engine_library)
   - Resource: [Valid Input and Return Types](https://domo-support.domo.com/s/article/000005173?language=en_US#input_variables)
3. Domo APIs and Authentication in Code Engine
   - Resource: [Developer Portal APIs Overview](https://developer.domo.com/portal/8ba9aedad3679-ap-is)
4. Exercise: Build a simple workflow that leverages a global Code Engine function
5. Exercise: Building a custom code engine package


## High-level Overview of Code Engine

   - [Intro to Code Engine Deck](https://domosoftware-my.sharepoint.com/:p:/g/personal/noah_finberg_domo_com/EVcupDM2TeZPsRes4c5jESUBMF27i-TK0mL5RP5b_zLP8A?e=uJLLNO)
   - Resource: [Code Engine KB Article](https://domo-support.domo.com/s/article/000005173?language=en_US)


## Anatomy of a Code Engine Function

- Reiterate benefit of leveraging Global Code Engine Functions
  - Managed and maintained by Domo
  - Accessible in all instances → easier to leverage in multi-instance architecture
  - Covers many of the Domo APIs that are undocumented
  - All code engine packages are versioned


- Explore Content Sharing Package
  - Explore code engine editor (note: you won't need to worry about the code of the function to actually use them, just good to see what goes into them)
  - Can see multiple versions - Domo will periodically update the package to add new  functions and to account for new code engine parameter types
  - Review left sidebar: Can see input and output parameters and expected types - types very important! Most common reason people get stuck.
  - Review sharePageWithGroup Function
    - Note: input is group type and pageId → share list of valid types.
    - Code Engine functions can call other code engine functions within same package
        - calls shareResource Function
            - highlight input parameters
            - highlight output parameters
            - highlight codeEngine.sendRequest → share list of codeEngine methods
              - Note: handles authentication (inherits authentication of current user) - to use other forms of authentication you'll need to write a customer package and pull in accounts (more in next exercise)
              - To make requests to external APIs you can use the axios library (JS) requests (Python) + accounts to pull in any auth credentials you may need to leverage

  - Test Function:
    - group type enables Domo to render picker dropdown (in Workflows/Forms/Queues) - when hitting function via API will just pass groupId

  - Highlight accounts part of UI - will be going through this in more detail in authentication exercise.



## Domo APIs and Authentication in Code Engine



## Exercise: Build a simple workflow that leverages a global Code Engine function



## Exercise: Building a custom code engine package