#include "echomesh/audio/Source.h"
#include "echomesh/audio/AudioPlayer.h"

namespace echomesh {
namespace audio {

Source::Source(const string& filename, int loops,
               long long begin, long long end, long long length,
               const string& device, int channels)
    : SampleAudioSource(filename, loops, begin, end, length),
      player_(AudioPlayer::getPlayer(device, channels))  {
  player_->addInputSource(this);
}

Source::~Source() {
  pause();
  unload();
  if (player_->removeInputSource(this))
    AudioPlayer::removePlayer(player_);
}

}  // namespace audio
}  // namespace echomesh