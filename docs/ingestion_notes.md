# Ingestion module - design notes (Week 2, Day 2)

## 1. Exceptions or assertions?
In `validate_record` I raise exceptions for a negative duration, but in
`IngestionReport.check_invariants` I use `assert`. Why is each the right tool there?

Assert is used to see if my own code is functioning properly. It's better to raise exceptions for when its a problem with something outside of my control.

## 2. Stop or collect?
Why is a malformed JSON file a `SourceError` that stops loading, while a record with
a bad status is a `RecordValidationError` that is collected? Who benefits from this split?

Because a bad JSON file has zero data we can trust. If only one record in a large file is broken, we can assume that the rest of the data is still good. It's not worth wasting that data

## 3. What did the context managers buy you?
Name two things that `open_source` / `LoadSession` do for the caller that you would otherwise
have to remember to do at every call site.

It closes the file for me so that it isn't always having to be closed in a try/catch/finally. It also turns low level errors into new exceptions so that not every call site needs to try and catch those exceptions.

## 4. Your hardest bad-input case
Which sample file or record took you longest to handle, and what was the cause?

I think doing loader.py took the longest since it had the most work and tied everything together. But getting started with contexts.py was also difficult.
