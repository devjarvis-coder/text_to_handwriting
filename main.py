import pywhatkit as pw

txt = """In this Python handwriting project, you will learn how to convert text to handwriting. It is a basic project 
that will help you with a better understanding of Python."""
pw.text_to_handwriting(txt, "demo1.png", [0, 0, 138])
print(" End ")
