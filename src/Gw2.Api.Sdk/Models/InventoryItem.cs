using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace Gw2.Api.Sdk.Models;

public class InventoryItem
{
    [JsonPropertyName("id")]
    public int Id { get; set; }

    [JsonPropertyName("count")]
    public int Count { get; set; }

    [JsonPropertyName("charges")]
    public int? Charges { get; set; }

    [JsonPropertyName("skin")]
    public int? Skin { get; set; }

    [JsonPropertyName("upgrades")]
    public int[]? Upgrades { get; set; }

    [JsonPropertyName("infusions")]
    public int[]? Infusions { get; set; }

    [JsonPropertyName("binding")]
    public string? Binding { get; set; }
}
