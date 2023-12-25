# Swing GUI Components README

This README provides a guide on how to create various Swing GUI components using the provided Python code. The code utilizes the `swingstrings` library for generating Swing code.

## Table of Contents

1. [Intro: swinpy](#swinpy)
2. [Container Components](#container-components)
    - [JFrame](#jframe)
    - [JPanel](#jpanel)
    - [JTabbedPane](#jtabbedpane)
3. [Interactive Elements](#interactive-elements)
    - [JLabel](#jlabel)
    - [JButton](#jbutton)
    - [JToggleButton](#jtogglebutton)
    - [JPasswordField](#jpasswordfield)
    - [JProgressBar](#jprogressbar)
    - [JTextField](#jtextfield)
    - [JCheckBox](#jcheckbox)
    - [JRadioButton](#jradiobutton)
    - [JComboBox](#jcombobox)
    - [JTextArea](#jtextarea)
4. [Examples](#examples)
    - [Hello World App](#example-1-hello-world-application)
    - [Login Form](#example-2-login-form-with-2-jlabels-and-2-jtextfields)
    - [3 buttons](#example-3-horizontal-layout-with-3-buttons)
    - [Tabbed View](#example-4-tabbed-view-with-two-tabs-each-containing-a-jtextarea)

---

## swinpy

Swinpy is a small application made with `swinpy`'s library, it can translate from python classes code to Java UI

## Container Components

### JFrame

```python
JFrame(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> padding=0,
    <Optional> name=<GeneratedString>,
    <Required> elements = [Element|Container...]
    <Required> layout = Vertical|Horizontal|FlowLayout
)
```

### JPanel

```python
JPanel(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> position = <CENTER|NORTH|SOUTH|EAST|WEST|LINE_END|LINE_START|PAGE_END|PAGE_START>
    <Optional> padding=0,
    <Optional> name=<GeneratedString>,
    <Required> elements = [Element|Container...]
    <Required> layout = Vertical|Horizontal|FlowLayout
)
```

### JTabbedPane

```python
JTabbedPane(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> position = <CENTER|NORTH|SOUTH|EAST|WEST|LINE_END|LINE_START|PAGE_END|PAGE_START>
    <Optional> padding=0,
    <Optional> name=<GeneratedString>,
    <Required> elements = [JPanel...] # does NOT support other elements
)
```

---

## Interactive Elements

### JLabel

```python
JLabel(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> position = <CENTER|NORTH|SOUTH|EAST|WEST|LINE_END|LINE_START|PAGE_END|PAGE_START>
    <Optional> padding=0,
    <Optional> name=<GeneratedString>,
    <Optional> text=<YourText>
)
```

### JButton

```python
JButton(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> position = <CENTER|NORTH|SOUTH|EAST|WEST|LINE_END|LINE_START|PAGE_END|PAGE_START>
    <Optional> padding=0,
    <Optional> name=<GeneratedString>,
    <Optional> label=<YourLabel>
)
```

#### Example Usage

```python
# Example usage to create a JButton
my_button = JButton(
    label="Click me", 
    foreground="red"
)
generated_code = my_button.build()  # Returns the generated JButton code
```

---

### JToggleButton

```python
JToggleButton(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> position = <CENTER|NORTH|SOUTH|EAST|WEST|LINE_END|LINE_START|PAGE_END|PAGE_START>
    <Optional> padding=0,
    <Optional> name=<GeneratedString>,
    <Optional> label=<YourLabel>,
    <Optional> selected=False
)
```

#### Example Usage

```python
# Example usage to create a JToggleButton
my_toggle_button = JToggleButton(
    label="Toggle", 
    selected=True
)
generated_code = my_toggle_button.build()  # Returns the generated JToggleButton code
```

---

### JPasswordField

```python
JPasswordField(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> position = <CENTER|NORTH|SOUTH|EAST|WEST|LINE_END|LINE_START|PAGE_END|PAGE_START>
    <Optional> padding=0,
    <Optional> name=<GeneratedString>
)
```

#### Example Usage

```python
# Example usage to create a JPasswordField
my_password_field = JPasswordField()
generated_code = my_password_field.build()  # Returns the generated JPasswordField code
```

---

### JProgressBar

```python
JProgressBar(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> position = <CENTER|NORTH|SOUTH|EAST|WEST|LINE_END|LINE_START|PAGE_END|PAGE_START>
    <Optional> padding=0,
    <Optional> name=<GeneratedString>,
    <Optional> value=0,
    <Optional> minimum=0,
    <Optional> maximum=100
)
```

#### Example Usage

```python
# Example usage to create a JProgressBar
my_progress_bar = JProgressBar(
    value=50, 
    foreground="green"
)
generated_code = my_progress_bar.build()  # Returns the generated JProgressBar code
```

---

### JTextField

```python
JTextField(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> position = <CENTER|NORTH|SOUTH|EAST|WEST|LINE_END|LINE_START|PAGE_END|PAGE_START>
    <Optional> padding=0,
    <Optional> name=<GeneratedString>,
    <Optional> title=<YourTitle>,
    <Optional> empty_border_pixels=0
)
```

#### Example Usage

```python
# Example usage to create a JTextField
my_text_field = JTextField(
    title="Enter Text", 
    empty_border_pixels=5
)
generated_code = my_text_field.build()  # Returns the generated JTextField code
```

---

### JCheckBox

```python
JCheckBox(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> position = <CENTER|NORTH|SOUTH|EAST|WEST|LINE_END|LINE_START|PAGE_END|PAGE_START>
    <Optional> padding=0,
    <Optional> name=<GeneratedString>,
    <Optional> label=<YourLabel>,
    <Optional> selected=False
)
```

#### Example Usage

```python
# Example usage to create a JCheckBox
my_check_box = JCheckBox(
    label="Check me", 
    selected=True, 
    background="cyan"
)
generated_code = my_check_box.build()  # Returns the generated JCheckBox code
```

---

### JRadioButton

```python
JRadioButton(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> position = <CENTER|NORTH|SOUTH|EAST|WEST|LINE_END|LINE_START|PAGE_END|PAGE_START>
    <Optional> padding=0,
    <Optional> name=<GeneratedString>,
    <Optional> label=<YourLabel>,
    <Optional> selected=False
)
```

#### Example Usage

```python
# Example usage to create a JRadioButton
my_radio_button = JRadioButton(
    label="Radio me", 
    foreground="blue"
)
generated_code = my_radio_button.build()  # Returns the generated JRadioButton code
```

---

### JComboBox

```python
JComboBox(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> position = <CENTER|NORTH|SOUTH|EAST|WEST|LINE_END|LINE_START|PAGE_END|PAGE_START>
    <Optional> padding=0,
    <Optional> name=<GeneratedString>,
    <Required> items=["Option 1", "Option 2", "Option 3"]
)
```

#### Example Usage

```python
# Example usage to create a JComboBox
my_combo_box = JComboBox(
    items=["Option 1", "Option 2", "Option 3"], 
    background="pink"
)
generated_code = my_combo_box.build()  # Returns the generated JComboBox code
```

---

### JTextArea

```python
JTextArea(
    <Optional> background="",
    <Optional> foreground="",
    <Optional> position = <CENTER|NORTH|SOUTH|EAST|WEST|LINE_END|LINE_START|PAGE_END|PAGE_START>
    <Optional> padding=0,
    <Optional> name=<GeneratedString>,
    <Optional> rows=0,
    <Optional> columns=0,
    <Optional> title=<YourTitle>
)
```

#### Example Usage

```python
# Example usage to create a JTextArea
my_text_area = JTextArea(
    rows=5, 
    columns=30, 
    title="Text Area", 
    foreground="black"
)
generated_code = my_text_area.build()  # Returns the generated JTextArea code
```

---

## Basic syntax

---

## Examples

### Example 1: Hello World Application

```python
# Hello World Application
JFrame(elements=[
    JLabel(text="Hello, Swing!")
], layout=Vertical)

```

### Example 2: Login Form with 2 JLabels and 2 JTextFields

```python
# Login Form with 2 JLabels and 2 JTextFields
JFrame(elements=[
    JLabel(text="Username:"),
    JTextField(name="username"),
    JLabel(text="Password:"),
    JTextField(name="password"),
], layout=Vertical)
```

### Example 3: Horizontal Layout with 3 Buttons

```python
JFrame(elements=[
    JButton(label="Button 1"),
    JButton(label="Button 2"),
    JButton(label="Button 3"),
], layout=Horizontal)
```

### Example 4: Tabbed View with Two Tabs, Each Containing a JTextArea

```python
JFrame(elements=[
    JTabbedPane(elements=[
        JPanel(elements=[
            JTextArea(title="Tab 1 Content", rows=10, columns=30)
        ]),
        JPanel(elements=[
            JTextArea(title="Tab 2 Content", rows=10, columns=30)
        ]),
    ])
])
```

Feel free to run these examples in your Python environment and customize them further according to your needs! If you have any questions or need additional examples, let me know!


## How to generate a swing form

To write and run the Swing GUI code using the `swinpy` library, follow these steps. Note that the code should be saved in a file with either a `.form` or `.txt` extension.

1. **Create a New File:**
   Open your preferred text editor (e.g., Notepad, Visual Studio Code, or any other code editor).

2. **Copy the Desired Example Code:**
   Choose one of the examples from the provided README, such as the "Hello World Application" or any other example that suits your needs. Copy the Python code for the chosen example.

3. **Paste Code into the File:**
   Paste the copied code into your text editor.

4. **Save the File:**
   Save the file with a `.form` or `.txt` extension. For example, you could name it `my_gui_code.form` or `my_gui_code.txt`. Ensure that you choose the correct file extension.

5. **Run the Code:**
   Open a terminal or command prompt, navigate to the directory where you saved the file, and run the Python script using the following command:

   ```bash
   swinpy my_gui_code.form  # Replace "my_gui_code.form" with your file name
   ```

   Make sure you have Python installed on your system.

6. **View the Generated Swing Code:**
   After running the script, the output will display the generated Swing code. You can use this code in your Java Swing project.

For each example, follow the same steps, choosing the appropriate example code, saving it to a file, and running it using Python.

Remember to customize the code as needed, and if you encounter any issues or have further questions, feel free to ask for assistance!
