
/-
$ \textbf{Theorem:} $
$ A \land B \Rightarrow B \land A $
-/
theorem test_theorem (A B : Prop) : A ∧ B → B ∧ A := by {
  /-
  $ \textbf{Proof:} $
  Assume that $ A \land B $ holds.
  -/
  intro h

  /-
  Then both propositions $ A $ and $ B $ are true.
  -/
  obtain ⟨a, b⟩ := h

  /-
  To prove $ B \land A $, we need to show both $ B $ and $ A $,
  but in reverse order.
  -/
  constructor

  /-
  Since we already have a proof for $ B $ and $ A $,
  it follows that $ B \land A $ holds.

  $ \blacksquare $
  -/
  exact b
  exact a
}
