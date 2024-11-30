using System;

class Puzle1
{
    static void Main()
    {
        string codigoC = "using System;\n\nclass Puzle1\n{\n    static void Main()\n    {\n        string codigoC = \"using System; class Puzle1 { static void Main() { string codigoC = `` string codigoJS =`` Console.WriteLine(codigoJS);}}\";\n        string codigoJS = $\"console.log(`{codigoC.Replace(\"`\", \"\\\\`\")}`);\";\n        Console.WriteLine(codigoJS);\n    }\n}";
        string codigoJS = $"console.log(`{codigoC.Replace("`", "\\`")}`);";
        Console.WriteLine(codigoJS);
    }
}
