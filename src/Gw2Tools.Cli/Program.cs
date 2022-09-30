using Mono.Options;
using Spectre.Console;
using System;

namespace Gw2Tools.Cli;

public static class Program
{
    public static void Main(string[] args)
    {
        string apiKey = AnsiConsole.Ask<string>("Input your GW2 API Key:");

        string command = AnsiConsole.Prompt(
            new SelectionPrompt<string>()
            .Title("What command would you like to run?")
            .PageSize(10)
            .AddChoices(new[]
            {
                "Fish Inventory", "PvPips"
            }));


    }
}