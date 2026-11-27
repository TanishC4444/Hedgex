# Completed source reconciliation

The maintained runtime has all shared backend functions from the three older desktop versions. AST comparison found identical bodies for the 29 shared functions in Hedgex_dist and PCIS_FantasySMG; finalSMGHedgex has 28 and lacks the newer fund-chart route. No older-only backend function was found.

Current source trees are preserved in `reconcile/current-desktop`, `reconcile/current-pcis`, and `reconcile/current-final-smg`, attached as merge parents to the maintained history. Their alternate templates remain browsable without mixing older designs into the running app. Source hashes and original source commit IDs are recorded in source-reconciliation.json.

Original local histories and original related repositories remain intact. Old compiled executable history includes files above GitHub's 100 MB limit, so it was not imported into this maintained repository. Runtime CSV balances and transaction records stay in the original local folders and were not overwritten.
