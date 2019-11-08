local M = {}

function M.sound(path)
	return [[sound: "]].. path ..[["
looping: 0
group: "master"
gain: 1.0
pan: 0.0
speed: 1.0
]]
end

function M.spine_scene(spine_json, atlas_path)
	spine_json = spine_json or ""
	atlas_path = atlas_path or ""
	return [[spine_json: "]] .. spine_json .. [["
atlas: "]] .. atlas_path  .. [["
sample_rate: 30
]]
end

function M.spine_model(path)
	return [[spine_scene: "]] .. path .. [["
default_animation: ""
skin: ""
]]
end


return M