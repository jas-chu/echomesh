#pragma once

#include "echomesh/color/FColorList.h"

namespace echomesh {
namespace color {

FColorList mirror(
    const FColorList&, unsigned int x, unsigned int y,
    bool reverseX, bool reverseY);

}  // namespace color
}  // namespace echomesh
