"use client";

import React, { useEffect } from "react";
import { invoke } from "@tauri-apps/api/tauri";
import { useSettingsStore } from "./stores/settings-store";

const DEBUG = true;

const Initialization: React.FC = () => {
  const { setSettings } = useSettingsStore();

  useEffect(() => {
    let osPlatform = "";
    // Make a call to the backend to get OS platform and set Radiance path
    invoke<string>("query_os_platform", {})
      .then(async (platform: any) => {
        if (DEBUG) {
          console.log("OS platform successfully queried:", platform);
        }
        // Default Radiance path for macOS and Linux
        let radianceDefaultPath = "/usr/local/radiance/bin";
        // If platform is windows, update default Radiance path
        if (osPlatform === "windows") {
          radianceDefaultPath = "C:\\Radiance\\bin";
        }

        // Get the saved paths to binaries and update settings
        const contents = await invoke<string>("read_binary_paths", {});
        let contentsObject;
        if (contents) {
          contentsObject = JSON.parse(contents);
        } else {
          contentsObject = { hdrgenpath: "", dcrawemupath: "" };
        }
        setSettings({
          radiancePath: radianceDefaultPath,
          hdrgenPath: contentsObject.hdrgenpath,
          dcrawEmuPath: contentsObject.dcrawemupath,
          outputPath: await invoke("get_default_output_path"), // queries backend for suggested place to store files
        });
        if (!contentsObject.hdrgenpath || !contentsObject.dcrawemupath) {
          alert(
            "Please enter the paths to the HDRGen and dcraw_emu binaries in the settings before generating HDR images."
          );
        }
      })
      .catch(() => {
        console.error;
      });
  }, [setSettings]);

  return null;
};

export default Initialization;