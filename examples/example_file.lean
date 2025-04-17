
/-
Theorem: A and B implies B and A
-/
theorem test_theorem (A B : Prop) : A ∧ B → B ∧ A := by {
  /-
  first we assume that (A and B) is true
  -/
  intro h
  /-
  we want to prove that (B and A) is also true.
  -/
  obtain ⟨a, b⟩ := h
  constructor
  exact b
  exact a
}
