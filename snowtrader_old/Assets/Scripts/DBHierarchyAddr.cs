public static class DBHierarchyAddr
{
    public const string gameManager = "GameManager";
    public const string resourceManager = "ResourceManager";
    public const string player = "Player";

    // HUD
    public const string HUD = "HUD";
    public const string HUDCanvas = HUD + "/Canvas";

    public const string HUDPlayerTempBar = HUDCanvas + "/PlayerTemperatureBar";

    public const string SelectedCraftItemContainer = HUDCanvas + "/SelectedCraftItemContainer";
    public const string SelectedCraftItem = SelectedCraftItemContainer + "/Image";
    public const string SelectedCraftItemCost = SelectedCraftItemContainer + "/Cost";


    public const string HUDCoin = HUDCanvas + "/HUDCoin";
    public const string HUDCoinValue = HUDCoin + "/Value";
    public const string HUDCoinCap = HUDCoin + "/Cap";

    public const string HUDWood = HUDCanvas + "/HUDWood";
    public const string HUDWoodValue = HUDWood + "/Value";
    public const string HUDWoodCap = HUDWood + "/Cap";

    public const string HUDWool = HUDCanvas + "/HUDWool";
    public const string HUDWoolValue = HUDWool + "/Value";
    public const string HUDWoolCap = HUDWool + "/Cap";

    // Chartacter Dialog
    public const string characterDialogBox = "CharacterDialogContainer";
    public const string dialogBoxCanvas = characterDialogBox + "/DialogBoxCanvas";
    public const string dialogBoxText = dialogBoxCanvas + "/Text";
    public const string dialogBoxSpeakerName = dialogBoxCanvas + "/SpeakerName";
    public const string dialogBoxSpeakerSprite = dialogBoxCanvas + "/Background/SpeakerFrame/SpeakerSprite";

    // Trading Dialog
    public const string tradingDialog = "TradingDialog";
    public const string tradingCanvas = tradingDialog + "/TradingCanvas";
    public const string tradingCurrentSelection = tradingCanvas + "/CurrentSelection";
    public const string tradingDialogItemPrefix = tradingCanvas + "/Item_";

    // Chop Wood
    public const string playerBars = player + "/PlayerBars/Canvas";
    public const string chopWoodProgressSlider = playerBars + "/ChopWoodProgressSlider";

    // Misc
    public const string ControllerButtonTooltip = player + "/ControllerButtonTooltip";
    public const string InitialCheckpoint = "Mimas_Area_01/Checkpoints/Obj_Bonfire_Eternal_1";
}
