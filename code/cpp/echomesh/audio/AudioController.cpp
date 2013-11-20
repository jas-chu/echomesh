#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>

#include "yaml-cpp/yaml.h"

#include "echomesh/audio/AudioController.h"
#include "echomesh/audio/SampleAudioSource.h"
#include "echomesh/network/SocketLineGetter.h"
#include "echomesh/util/GetDevice.h"
#include "rec/util/STL.h"

namespace echomesh {
namespace audio {

using namespace std;

AudioController::AudioController(const Node& node) : node_(node) {
}

void AudioController::audio() {
  const Node& data = node_["data"];
  string type;
  Hash hash;
  data["type"] >> type;
  data["hash"] >> hash;
  audio::SampleAudioSource*& source = sources_[hash];

  log("Receiving " + type);
  if (type == "construct") {
    if (source) {
      log("Warning: already created a source for hash " + String(hash));
      return;
    }
    source = new audio::SampleAudioSource(data);
    mixerAudioSource_.addInputSource(source, true);
    return;
   }

  if (not source) {
    log("No source?? " + type);

  } else if (type == "run") {
    log("run");
    source->run();

  } else if (type == "begin") {
    log("begin");
    source->begin();

  } else if (type == "pause") {
    log("pause");
    source->pause();

  } else if (type == "unload") {
    sources_.erase(hash);
    mixerAudioSource_.removeInputSource(source);
  }
}

}  // namespace audio
}  // namespace echomesh
