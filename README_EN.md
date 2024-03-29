# Customer creditworthiness evaluation model
[Chinese](./README.md) | [English]
## Background
A bank has 2,000 rows of data on whether customers are untrustworthy, and the bank wants to build a model to predict whether future target customers meet the bank's untrustworthy standards, so as to facilitate the decision to accept the customer's credit card application.

## Application Interface
Run the commnand "streamlit run interface.py" on command line to run this application
Or click the link https://fent1-advancedpython-interface-evd5ob.streamlit.app/ to access my application.

It is an Interactive Interface that sales representatives in a bank/credit card company can use to decide on accepting or rejecting applications. 
<img width="1469" alt="image" src="https://user-images.githubusercontent.com/43925272/235272039-beb82fec-a227-48f7-8250-668b4169538c.png">

The prediction model is based on Gradient Boost model, which has 72.73% test score.
