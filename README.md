# PSON: Python Simple Object Notation

## Tired of JSON? We are too.

Ah, JSON. The supposed "lightweight data-interchange format." Sure, it's easy for machines to parse and generate, but have you ever tried writing it by hand? Yes, because nothing says "user-friendly" quite like typing endless braces, quotes, and commas, only to have a tiny syntax error throw everything into chaos. What's that, JSON? A single missing comma? Well, I guess my entire weekend is ruined now.

Enter **PSON**, the Python Simple Object Notation. It's JSON, but for people who actually want to *enjoy* their coding. Forget about JavaScript's syntax rules and embrace the beauty of Python syntax. No more unnecessary double quotes, no more tears—just Python goodness in all its simplicity.

## Why PSON?

1. **It's JSON without the nonsense**: Let's be honest, JSON's syntax is unnecessarily complicated. Why do I need double quotes around every key? Why does a trailing comma launch a thousand errors? With PSON, you just write Python syntax. Simple, readable, and—dare I say—enjoyable.

2. **Helpful Error Messages**: JSON errors are like cryptic prophecies. They tell you *something* is wrong, but not what or where. PSON takes a different approach. It gives you *actual helpful messages* so you can fix your mistakes quickly instead of embarking on a journey of despair.

3. **Python Developers Rejoice**: You know Python. You like Python. So why are you using a JavaScript notation format for your data? PSON lets you write your data the way nature intended: with Python syntax.

## How to Use PSON

### Installation

You can install PSON directly from PyPI (once we get around to publishing it):

```sh
pip install pson
```

### Example Usage

```python
from pson import PSON

# Define your data using Python syntax
pson_str = """
{
    'name': 'Alice',
    'age': 30,
    'is_student': False,
    'hobbies': ['reading', 'hiking', 'coding']
}
"""

# Parse PSON string to Python object
data = PSON.loads(pson_str)
print(data)

# Convert Python object to PSON string
pson_string = PSON.dumps(data)
print(pson_string)
```

### What Makes PSON Great?

- **No More Quotation Madness**: JSON makes you type `"` everywhere. PSON says, "Nah, single quotes are fine."
- **No More Brace Anxiety**: JSON demands your complete obedience to commas and braces. PSON? It's as chill as a hammock in a summer breeze.
- **Human-Readable**: JSON is for machines. PSON is for humans who like Python. You deserve better than JavaScript's leftovers.

## Important Disclaimer

**PSON is not JSON.** Don't try to fool a JavaScript parser with it, or you'll have a bad time. PSON is for Python developers who want to work with a more human-friendly alternative to JSON *within Python*. When it's time to send your data to a JavaScript-based API, feel free to cry and use regular JSON.

## Contributing

If you also hate JSON and think PSON is the future, feel free to contribute! Submit pull requests, report issues, or just come by and complain about JSON with us.

## License

MIT License. Because we're nice like that.

---

*PSON: Making data serialization suck less, one Python dictionary at a time.*

