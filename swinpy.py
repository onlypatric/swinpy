from dataclasses import dataclass, field
import os
from typing import List, Union
import swingstrings
from enum import Enum


class Position(Enum):
    CENTER = "CENTER"
    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"
    LINE_END = "LINE_END"
    LINE_START = "LINE_START"
    PAGE_END = "PAGE_END"
    PAGE_START = "PAGE_START"


def parseColor(color:str):
    named_colors = {
        'black': "Color.BLACK",
        'blue': "Color.BLUE",
        'cyan': "Color.CYAN",
        'gray': "Color.GRAY",
        'green': "Color.GREEN",
        'magenta': "Color.MAGENTA",
        'orange': "Color.ORANGE",
        'pink': "Color.PINK",
        'red': "Color.RED",
        'white': "Color.WHITE",
        'yellow': "Color.YELLOW",
    }
    if color in named_colors:
        return named_colors[color]
    else:
        return f"Color.decode(\"{color}\")"
class ClassNameGenerator:
    def __init__(self):
        self.used_names = set()

    def generate_unique_name(self, class_name):
        base_name = class_name.lower()
        count = 1
        unique_name = f"{base_name}_{count}"
        while unique_name in self.used_names:
            count += 1
            unique_name = f"{base_name}_{count}"
        self.used_names.add(unique_name)
        return unique_name


name_generator = ClassNameGenerator()
@dataclass
class Element:
    background: str = ""
    foreground: str = ""
    padding: int = 0
    name: str = field(default_factory=str)


class Vertical:
    def __str__(self) -> str:
        return "vertical"

class FlowLayout:
    def __str__(self) -> str:
        return "flowlayout"

class Horizontal:
    def __str__(self) -> str:
        return "horizontal"


class BorderLayout:
    def __str__(self) -> str:
        return "borderlayout"


@dataclass
class Container(Element):
    elements: List[Element] = field(default_factory=list)
    layout: Union[Vertical, Horizontal] = None


@dataclass
class JFrame(Container):
    name: str = "JFrame"

    def build(self):
        layt = "null"
        if self.layout == None or self.layout == Vertical:
            layt = "new BoxLayout(cp, BoxLayout.PAGE_AXIS)"
        elif self.layout == Horizontal:
            layt = "new BoxLayout(cp, BoxLayout.LINE_AXIS)"
        elif self.layout == FlowLayout:
            layt = "new FlowLayout()"
        elif self.layout == BorderLayout:
            layt = "new BorderLayout()"
        children = self.buildChildren()
        return swingstrings.JFRAME_STR.replace("{LAYOUT}", layt).replace("{CHILDS}", "\n".join(children))

    def buildChildren(self):
        children = []
        for element in self.elements:
            extra = ""
            if self.layout==BorderLayout:
                if element.position is None:
                    element.position=Position.CENTER
                extra = f", BorderLayout.{element.position.value}"
            children.append(
                f"{element.build()}\n        cp.add({element.name}{extra});")
        return children


@dataclass
class JPanel(Container):
    scrollable: bool = False
    name: str = ""
    title: str = None
    position: Position = Position.CENTER

    def build(self):
        layt = "null"
        self.name = name_generator.generate_unique_name("JPanel") if not self.name or self.name in name_generator.used_names else self.name
        if self.layout == None or self.layout == Vertical:
            layt = f"new BoxLayout({self.name}, BoxLayout.PAGE_AXIS)"
        elif self.layout == Horizontal:
            layt = f"new BoxLayout({self.name}, BoxLayout.LINE_AXIS)"
        elif self.layout == FlowLayout:
            layt = "new FlowLayout()"
        elif self.layout == BorderLayout:
            layt = "new BorderLayout()"
        children = self.buildChildren()
        x = [ f"        JPanel {self.name} = new JPanel();\n",
               f"        {self.name}.setBackground({parseColor(self.background)});\n" if self.background else "",
               f"        {self.name}.setForeground({parseColor(self.foreground)});\n" if self.foreground else "",
               f"        {self.name}.setBorder(new TitledBorder(\"{self.title}\"));" if self.title else "",
               f"        {self.name}.setBorder(new EmptyBorder({self.padding},{self.padding},{self.padding},{self.padding}));" if self.padding > 0 and not self.title else "",
               f"        {self.name}.setLayout({layt});\n"+"\n".join(children),
               f"        JScrollPane {self.name}ScrollPane = new JScrollPane({self.name});" if self.scrollable else ""]
        if self.scrollable:
            self.jpanelName = self.name
            self.name = f"{self.name}ScrollPane"
        return "".join(x)

    def buildChildren(self):
        children = []
        for element in self.elements:
            extra = ""
            if self.layout==BorderLayout:
                if element.position is None:
                    element.position=Position.CENTER
                extra = f", BorderLayout.{element.position.value}"
            if type(element) == JPanel:
                element.name = name_generator.generate_unique_name("JPanel") if not self.name else self.name
            children.append(
                f"{element.build()}\n        {self.name}.add({element.name}{extra});")
        return children

@dataclass
class InteractiveElement(Element):
    position: Position = Position.CENTER
    actionListener:bool=False

    def build(self):
        return f"        {self.name}.addActionListener(e->{{}})" if self.actionListener else ""


@dataclass
class JLabel(InteractiveElement):
    text: str = None

    def build(self):
        self.name = name_generator.generate_unique_name("JLabel") if not self.name else self.name
        x = [ f"        JLabel {self.name} = new JLabel(\"{self.text}\");\n",
               f"        {self.name}.setBackground({parseColor(self.background)});\n" if self.background else "",
               f"        {self.name}.setForeground({parseColor(self.foreground)});\n" if self.foreground else "",
               f"        {self.name}.setBorder(new EmptyBorder({self.padding},{self.padding},{self.padding},{self.padding}));" if self.padding>0 else "",
               super().build()]
        return "".join(x)


@dataclass
class JButton(InteractiveElement):
    label: str = ""

    def build(self):
        self.name = name_generator.generate_unique_name("JButton") if not self.name else self.name
        x = [ f"        JButton {self.name} = new JButton(\"{self.label}\");\n",
               f"        {self.name}.setBackground({parseColor(self.background)});\n" if self.background else "",
               f"        {self.name}.setForeground({parseColor(self.foreground)});\n" if self.foreground else "",
               f"        {self.name}.setBorder(new EmptyBorder({self.padding},{self.padding},{self.padding},{self.padding}));" if self.padding>0 else "",
              super().build()]
        return "".join(x)


@dataclass
class JToggleButton(InteractiveElement):
    label: str = ""
    selected: bool = False

    def build(self):
        self.name = name_generator.generate_unique_name("JToggleButton") if not self.name else self.name
        x = [f"        JToggleButton {self.name} = new JToggleButton(\"{self.label}\", {str(self.selected).lower()});\n",
             f"        {self.name}.setBackground({parseColor(self.background)});\n" if self.background else "",
             f"        {self.name}.setForeground({parseColor(self.foreground)});\n" if self.foreground else "",
             f"        {self.name}.setBorder(new EmptyBorder({self.padding},{self.padding},{self.padding},{self.padding}));" if self.padding>0 else "",
             super().build()]
        return "".join(x)


@dataclass
class JPasswordField(InteractiveElement):
    def build(self):
        self.name = name_generator.generate_unique_name("JPasswordField") if not self.name else self.name
        x = [f"        JPasswordField {self.name} = new JPasswordField();\n",
             f"        {self.name}.setBackground({parseColor(self.background)});\n" if self.background else "",
             f"        {self.name}.setForeground({parseColor(self.foreground)});\n" if self.foreground else "",
             f"        {self.name}.setBorder(new EmptyBorder({self.padding},{self.padding},{self.padding},{self.padding}));" if self.padding > 0 else "", 
             super().build()]
        return "".join(x)


@dataclass
class JTabbedPane(Container):
    position:Position = Position.CENTER
    def build(self):
        self.name = name_generator.generate_unique_name("JTab") if not self.name else self.name
        children = self.buildChildren()
        x = [f"        JTabbedPane {self.name} = new JTabbedPane();\n",
             f"        {self.name}.setBackground({parseColor(self.background)});\n" if self.background else "",
             f"        {self.name}.setForeground({parseColor(self.foreground)});\n" if self.foreground else "",
             f"        {self.name}.setBorder(new EmptyBorder({self.padding},{self.padding},{self.padding},{self.padding}));\n" if self.padding > 0 else "",
             f"        {self.name}.setTabLayoutPolicy(JTabbedPane.SCROLL_TAB_LAYOUT);", "\n".join(children),
             super().build()]
        return "".join(x)

    def buildChildren(self):
        children = []
        for element in self.elements:
            if type(element) == JPanel:
                element.name = name_generator.generate_unique_name("JPanel") if not self.name else self.name
                children.append(
                    f"{element.build()}\n        {self.name}.addTab(\"{element.name}\", {element.name});")
        return children


@dataclass
class JProgressBar(InteractiveElement):
    value: int = 0
    minimum: int = 0
    maximum: int = 100

    def build(self):
        self.name = name_generator.generate_unique_name("JProgressBar") if not self.name else self.name
        x = [f"        JProgressBar {self.name} = new JProgressBar({self.minimum}, {self.maximum});\n",
             f"        {self.name}.setValue({self.value});\n",
             f"        {self.name}.setBackground({parseColor(self.background)});\n" if self.background else "",
             f"        {self.name}.setForeground({parseColor(self.foreground)});\n" if self.foreground else "",
             f"        {self.name}.setBorder(new EmptyBorder({self.padding},{self.padding},{self.padding},{self.padding}));" if self.padding>0 else "",
             super().build()]
        return "".join(x)

@dataclass
class JTextField(InteractiveElement):
    title:str = None
    def build(self):
        self.name = name_generator.generate_unique_name("JTextField") if not self.name else self.name
        x = [ f"        JTextField {self.name} = new JTextField();\n",
               f"        {self.name}.setBackground({parseColor(self.background)});\n" if self.background else "",
               f"        {self.name}.setForeground({parseColor(self.foreground)});\n" if self.foreground else "",
               f"        {self.name}.setBorder(new TitledBorder(\"{self.title}\"));" if self.title else "",
              f"        {self.name}.setBorder(new EmptyBorder({self.padding},{self.padding},{self.padding},{self.padding}));" if self.padding > 0 and not self.title else "", 
              super().build()]
        return "".join(x)


@dataclass
class JCheckBox(InteractiveElement):
    label: str = ""
    selected: bool = False

    def build(self):
        self.name = name_generator.generate_unique_name("JCheckBox") if not self.name else self.name
        x = [ f"        JCheckBox {self.name} = new JCheckBox(\"{self.label}\", {str(self.selected).lower()});\n",
               f"        {self.name}.setBackground({parseColor(self.background)});\n" if self.background else "",
               f"        {self.name}.setForeground({parseColor(self.foreground)});\n" if self.foreground else "",
               f"        {self.name}.setBorder(new EmptyBorder({self.padding},{self.padding},{self.padding},{self.padding}));" if self.padding>0 else "",
              super().build()]
        return "".join(x)


@dataclass
class JRadioButton(InteractiveElement):
    label: str = ""
    selected: bool = False

    def build(self):
        self.name = name_generator.generate_unique_name("JRadioButton") if not self.name else self.name
        x = [ f"        JRadioButton {self.name} = new JRadioButton(\"{self.label}\", {str(self.selected).lower()});\n",
               f"        {self.name}.setBackground({parseColor(self.background)});\n" if self.background else "",
               f"        {self.name}.setForeground({parseColor(self.foreground)});\n" if self.foreground else "",
               f"        {self.name}.setBorder(new EmptyBorder({self.padding},{self.padding},{self.padding},{self.padding}));" if self.padding>0 else "",
              super().build()]
        return "".join(x)


@dataclass
class JComboBox(InteractiveElement):
    items: List[str] = field(default_factory=list)

    def build(self):
        self.name = name_generator.generate_unique_name("JComboBox") if not self.name else self.name
        items_str = ", ".join('"{}"'.format(item) for item in self.items)
        x =   [f"        JComboBox<String> {self.name} = new JComboBox<String>(new String[]{{ {items_str} }});\n",
               f"        {self.name}.setBackground({parseColor(self.background)});\n" if self.background else "",
               f"        {self.name}.setForeground({parseColor(self.foreground)});\n" if self.foreground else "",
               f"        {self.name}.setBorder(new EmptyBorder({self.padding},{self.padding},{self.padding},{self.padding}));" if self.padding>0 else "",
               super().build()]
        return "".join(x)


@dataclass
class JTextArea(InteractiveElement):
    rows: int = 0
    columns: int = 0
    title:str=None

    def build(self):
        self.name = name_generator.generate_unique_name("JTextArea") if not self.name else self.name
        x = [f"        JTextArea {self.name} = new JTextArea({self.rows}, {self.columns});\n" if (self.rows+self.columns) > 0 else f"        JTextArea {self.name} = new JTextArea();\n",
               f"        {self.name}.setBackground({parseColor(self.background)});\n" if self.background else "",
               f"        {self.name}.setForeground({parseColor(self.foreground)});\n" if self.foreground else "",
               f"        {self.name}.setBorder(new TitledBorder(\"{self.title}\"));" if self.title else "",
               f"        {self.name}.setBorder(new EmptyBorder({self.padding},{self.padding},{self.padding},{self.padding}));" if self.padding > 0 and not self.title else "",
             super().build()]
        return "".join(x)
