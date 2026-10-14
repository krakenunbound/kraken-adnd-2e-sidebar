--
-- AD&D 2E: the Menu Style option (Options > Menu Style) defaults to Sidebar.
--
-- The 2E ruleset registers OPTIONS_MENU with "menus" as its default, so a
-- player who never opened Options gets the top Menus / Records / Books bar.
-- The option is per user (stored on each player's computer); only its default
-- changes here, so anyone who chooses Menus keeps that choice. The desktop
-- reads the option when its windows are created, after every script's
-- onInit, so setting the default here is in time.
--

function onInit()
	if OptionsManager and OptionsManager.setOptionDefault then
		OptionsManager.setOptionDefault("OPTIONS_MENU", "sidebar");
	end
end
