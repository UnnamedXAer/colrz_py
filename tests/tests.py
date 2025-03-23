import colrz as c


# with method
print(c.yellow("\nThe tree is yellow."))

# with const
print("\n%sThe tree is red.%s" % (c.fg_red, c.fg_reset))

# background color
print("\n%s" % c.blue_bg(c.yellow("The tree is green with blue leafs.")))

print(
    "\n%s"
    % c.white_bg(
        c.green("The tree is green and ") + c.yellow("yellow with white leafs.")
    ),
)

print(
    "\n%s"
    % c.yellow(
        c.magenta_bg("The tree is yellow ") + c.cyan_bg(" with colorful leafs.")
    ),
)

text = f"\n{c.bg_white}|{c.fg_red}The tree is {c.bg_cyan} yellow with {c.fg_black}colorful leafs.{c.bg_reset}{c.fg_reset}. Done"
print(text)

text = f"\n{c.fg_red}The tree is {c.bg_cyan} yellow with {c.fg_yellow}colorful{c.bg_reset} leafs.{c.fg_reset}. Done"
print(text)

print(c.fg_green)
print("The tree is yellow.", end="")

print(c.bg_white)
print("The tree is yellow.", end="")

print(c.bg_reset)

print("The tree is yellow.", end="")

print(c.fg_reset)

print("The tree is yellow.")
