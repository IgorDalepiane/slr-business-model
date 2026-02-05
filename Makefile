# Project root: delegate PDF build to ieee_journal_slr
.PHONY: pdf clean

pdf:
	$(MAKE) -C ieee_journal_slr pdf

clean:
	$(MAKE) -C ieee_journal_slr clean
