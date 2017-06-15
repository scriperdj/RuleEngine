# Rule Engine Challenge (Evn: Python 3.5)

> Apply rules on input data signals and prints the name of signal which violates a rule. It skips records which satisfies a rule or if no matching rule found.

## Conceptual approach

The code `rule_engine.py` loads the rules data from `rules.json` file in run time memory. Then it loops through raw data from `raw_data.json` and checks if it satisfies a rule. If any data signal is not satisfied by a rule, the name of the signal is printed in console.

### rules.json
- It contains single JSON object with signal_name & value_type as keys (eg: ATL2_String). This is because the raw data had different value_types for a signal and a rule shall be applied only to the signal data which matches the value_type.
- A rule object can have cond & value keys. The cond could be `[eq,ne,lt,gt,le,ge]` which are transilated to `[==,!=,<,>,<=,>=]` conditional operators. And value has the conditional value.
(note: The Datetime value can have either `current` or date in `YYYY-MM-DD HH:MM:SS` format)
- The verbose rule `ATL1 value should not rise above 240.00` could be provided as below in rules file.
```js
{
	"ATL1_Integer": {
		"cond": "lt",
		"value": 240.00
	}
}
```
- The rule `ATL3 should not be in future` could be transilated as below.
```js
{
	"ATL3_Datetime": {
		"cond": "lt",
		"value": "current"
	}
}
```

## Trade-offs

The input files are hardcoded, so changing changing location or name of files need code changes. Also the value_types are hardcoded. If there is a new value_type that needs to be handled, the code needs modifications.

## Performance & bottlenecks

The code executes fine for small data. If the raw data & rules are large, this is a bad approach. The rules could be loaded in a Redis / Elasticsearch cluster for reference instread of loading all of them in memory.  Instead of reading whole raw data in execution time, the streaming data sould be inserted to a PubSub or queue services (like SQS) and processed as and when data arrives.

## Improvements

- The above mentioned optimizations could be made to overcome the bottlenecks.
- A UI which converts the verbose rule into JSON in required format.
