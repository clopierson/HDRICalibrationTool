import React, { useState, useEffect } from "react";
import SaveConfigDialog from "./save-config-dialog";
import LoadConfigDialog from "./load-config-dialog";
import { getName, getTauriVersion, getVersion } from "@tauri-apps/api/app";
import { invoke } from "@tauri-apps/api/tauri";

export default function ButtonBar({
  responsePaths,
  fe_correctionPaths,
  v_correctionPaths,
  nd_correctionPaths,
  cf_correctionPaths,
  viewSettings,
  setConfig,
  handleGenerateHDRImage,
}: any) {
  const [showSaveConfigDialog, setShowSaveConfigDialog] = useState<boolean>(false);
  const [showLoadConfigDialog, setShowLoadConfigDialog] = useState<boolean>(false);
  const [appVersion, setAppVersion] = useState<string>("");
  const [appName, setAppName] = useState<string>("");
  const [tauriVersion, setTauriVersion] = useState<string>("");
  const [savedConfigs, setSavedConfigs] = useState<[]>([]);

  // Loads the saved configurations from app config dir using a backend command
  async function getSavedConfigs() {
    const json: string = await invoke("get_saved_configs");
    const configs = JSON.parse(json).configurations;
    setSavedConfigs(configs);
  }

  useEffect(() => {
    // Retrieves app name, app version, and tauri version from Tauri API
    async function fetchAppInfo() {
      setAppVersion(await getVersion());
      setAppName(await getName());
      setTauriVersion(await getTauriVersion());
    }

    getSavedConfigs();
    fetchAppInfo();
  }, []);

  return (
    <div className="fixed bottom-0 left-0 w-full bg-gray-300 flex justify-around py-4">
      <button
        onClick={() => setShowLoadConfigDialog(!showLoadConfigDialog)}
        className="w-max bg-gray-600 hover:bg-gray-500 text-gray-300 font-semibold py-1 px-4 border-gray-400 rounded"
      >
        Load Configuration
      </button>
      <button
        onClick={() => setShowSaveConfigDialog((prev: any) => !prev)}
        className="w-max bg-gray-600 hover:bg-gray-500 text-gray-300 font-semibold py-1 px-4 border-gray-400 rounded"
      >
        Save Configuration
      </button>
      {showSaveConfigDialog && (
        <SaveConfigDialog
          config={{
            response_paths: responsePaths,
            fe_correction_paths: fe_correctionPaths,
            v_correction_paths: v_correctionPaths,
            nd_correction_paths: nd_correctionPaths,
            cf_correction_paths: cf_correctionPaths,
            diameter: viewSettings.diameter,
            xleft: viewSettings.xleft,
            ydown: viewSettings.ydown,
            target_res: viewSettings.targetRes,
            vh: viewSettings.vh,
            vv: viewSettings.vv,
          }}
          savedConfigs={savedConfigs}
          setSavedConfigs={setSavedConfigs}
          toggleDialog={() => setShowSaveConfigDialog(!showSaveConfigDialog)}
        />
      )}
      
      {showLoadConfigDialog && (
        <LoadConfigDialog
          setConfig={setConfig}
          savedConfigs={savedConfigs}
          getSavedConfigs={getSavedConfigs}
          toggleDialog={() => setShowLoadConfigDialog(!showLoadConfigDialog)}
        />
      )}
      <button
        onClick={handleGenerateHDRImage}
        className="w-max bg-osu-beaver-orange hover:bg-osu-luminance text-white font-semibold py-1 px-2 border-gray-400 rounded"
      >
        Generate HDR Image
      </button>
    </div>
  );
}