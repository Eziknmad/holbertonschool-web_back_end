export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    // const is block-scoped: inner declarations do not overwrite outer ones
  }

  return [task, task2];
}
