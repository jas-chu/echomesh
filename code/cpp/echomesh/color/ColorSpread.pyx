import six

def _even_color_slots(int size, int slots):
  slot = 0
  for i in range(slots):
    previous = slot
    slot = int(math.ceil(((i + 1) * size) / slots))
    yield slot - previous - 1

def _to_list(s, base_type, **kwds):
  if not s:
    return []
  if not isinstance(s, list):
    if isinstance(s, six.string_types):
      s = [i.strip() for i in s.split(', ')]
    elif isinstance(s, tuple):
      s = list(s)
    else:
      s = [s]
  return [i if isinstance(i, base_type) else base_type(i, **kwds) for i in s]

def _ensure_length(list x, int length):
  if len(x) < length:
    x.extend([x[-1]] * length - len(x))
  else:
    while len(x) > length:
      x.pop()

def color_spread(colors2, model, max_steps=None, steps=None, total_steps=None, transform=None):
  cdef Color c1
  cdef Color c2
  cdef FColor f1
  cdef FColor f2

  if not colors2 or len(colors2) <= 1:
    raise Exception('spread: There must be at least two colors.')

  if not (steps is None or total_steps is None):
    raise ValueError('spread: Can only set one of steps and total_steps')

  cdef ColorList colors
  colors = ColorList(colors2, model=model)
  # print('!!!!', colors2, colors)
  # colors = _to_list(colors, Color, model=model)
  transform = _to_list(transform, Transform)
  lc = len(colors)
  if transform:
    _ensure_length(transform, lc - 1)

  if steps:
    _ensure_length(steps, lc - 1)
  else:
    steps = list(_even_color_slots((total_steps or max_steps) - 1, lc - 1))

  steps = list(steps)
  cl = ColorList(model=model)
  cl.thisptr.resize(sum(steps) + lc)
  pos = 0
  for i, step in enumerate(steps):
    c1 = colors[i]
    c2 = colors[i+1]
    f1 = c1.thisptr[0]
    f2 = c2.thisptr[0]
    # print('!!!!', i, c1, c2)
    tr = (transform and transform[i].apply) or (lambda x: x)
    for j in range(step + 2):
      inc = tr(j / (step + 1.0))
      cl.thisptr.set(cl._model.interpolate(f1, f2, inc), pos)
      pos += 1
    pos -= 1

  return cl

def even_color_spread(steps, *colors):
  return color_spread(colors, None, steps, None, None, None)
