export function getLevelInfo(state) {
  const level = state.student.level;
  const activeCredits = state.student.activeCredits;
  const nextLevel = state.levels[level + 1] || state.levels[level];
  const maxCredits = nextLevel.credits;
  return { level, activeCredits, maxCredits };
}
