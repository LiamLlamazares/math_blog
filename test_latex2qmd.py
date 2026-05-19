import unittest
import sys
from io import StringIO
from latex2qmd import convert_body

class TestLatex2Qmd(unittest.TestCase):
    def test_starred_align_conversion(self):
        latex_input = r"""
        \begin{align*}
        \Ll _\gamma := \Ll + \gamma \bm{I}
        \end{align*}
        """
        output = convert_body(latex_input)
        
        # Verify that align* was parsed and preserved without escaped backslashes in front of asterisk
        self.assertIn(r"\begin{align*}", output)
        self.assertIn(r"\end{align*}", output)
        self.assertNotIn(r"\begin{align\*}", output)
        self.assertNotIn(r"\end{align\*}", output)

    def test_starred_equation_conversion(self):
        latex_input = r"""
        \begin{equation*}
        E = mc^2
        \end{equation*}
        """
        output = convert_body(latex_input)
        
        # Verify that equation* was parsed and preserved without escaped backslashes in front of asterisk
        self.assertIn(r"\begin{equation*}", output)
        self.assertIn(r"\end{equation*}", output)
        self.assertNotIn(r"\begin{equation\*}", output)
        self.assertNotIn(r"\end{equation\*}", output)

    def test_normal_align_conversion(self):
        latex_input = r"""
        \begin{align}
        a = b
        \end{align}
        """
        output = convert_body(latex_input)
        
        # Verify normal align works
        self.assertIn(r"\begin{align}", output)
        self.assertIn(r"\end{align}", output)

    def test_unmatched_math_environment_warning(self):
        latex_input = r"""
        \begin{align*}
        \Ll _\gamma := \Ll + \gamma \bm{I}
        \end{align5}
        """
        # Capture sys.stderr
        captured_stderr = StringIO()
        sys.stderr = captured_stderr
        
        try:
            output = convert_body(latex_input)
        finally:
            sys.stderr = sys.__stderr__
            
        warning_msg = captured_stderr.getvalue()
        
        # Check that we received the warning for unmatched math environment
        self.assertIn("WARNING: Unmatched math environment \\begin{align*} (no matching \\end found).", warning_msg)

if __name__ == "__main__":
    unittest.main()
