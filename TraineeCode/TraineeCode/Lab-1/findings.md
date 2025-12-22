# Lab-1 Findings

- Running the program prints two sections: Manager1 shows AccNo 004701, Balance 45000.0; Manager2 shows AccNo ICI004701, Balance 48825.0 (includes 8.5% interest once).
- `Account` uses class-level defaults and no `__init__`, so instance state is only set after the first assignment—unclear and easy to misuse.
- `AccountManager1` sets the private fields directly, so it skips the bank-code prefix and the interest calculation (breaks encapsulation).
- `AccountManager2` uses the properties, so the acc_no setter adds the ICI prefix and the balance getter adds the computed interest.
- `compute_interest` is simple interest (8.5% of principal) added whenever balance is read; repeated reads keep reporting principal + that interest amount.
- `program.py` finishes with `input()`, so it will block if there is no user input; pipe a newline or remove it for unattended runs.
