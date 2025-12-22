Filled in the missing fill_account_data so the account gets valid values.

Change: fill_account_data now sets acc_no, name, and balance via the property setters, applying the ICI prefix and interest logic. See account_manager.py:7-16.
Why: Previously it was pass, so acc_no stayed None and display_account_data crashed when concatenating. Now the program runs and prints the account details.