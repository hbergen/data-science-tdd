# Definitions

[Common testing concepts](https://medium.com/pacroy/separate-unit-integration-and-functional-tests-for-continuous-delivery-f4dc240d8f2f) which frequently apply to data science projects.

## Data validation tests
**Definition**
> Test the quality of data that is used throughout the project and which may change over time.

**Why is this important to test?**

If underlying data is corrupted, the entire pipeline will be affected.

**What to test? (Examples)**
* Data is the correct type
* Data contains no nulls
* Data is within an expected range

## Unit tests
**Definition**
> Test the performance of a specific function.

**Why is this important to test?**

If changes are made to the code over time, this will ensure that these fundamental functions are still operating as expected. This type of issue could be more common if there are multiple users working on a project.

**What to test? (Examples)**
* Function to implement accuracy score still produces expected result

## Integration tests

**Definition**
> Test how well pieces of your code run together. Can use a "stub" (mocked data) to isolate code issues from data validation issues. Integration tests that test the entire pipeline are called *functional tests*.

**Why is this important to test?**

Integration tests will identify breakages in behavior to modules which are dependencies.

**What to test? (Examples)**
* Function to process data still produces expected result
* Predicted values are within an expected range. This might break if a feature transformation is added in a prior step, and adjustment were not made later on to invert the predictions.
