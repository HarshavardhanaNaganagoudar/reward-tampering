# Reward Tampering in LLM Agents

An experimental study investigating whether an LLM agent independently modifies its own reward functions when given direct file-editing access.

## Objective

Explore whether an autonomous LLM agent chooses to modify, remove, or introduce reward functions when given control over its reward structure, without explicitly instructing it to do so.

## Experimental Setup

- **Model:** Gemma 4 12B
- **Runtime:** Ollama
- **Language:** Python
- **Interaction:** Tool-based file access

The agent can:
- Read existing reward functions.
- Modify or remove existing functions.
- Introduce new reward functions.
- Inspect its modifications.

Human operators cannot directly modify the reward file during an experiment.

## Project Structure

```text
reward-tampering/
├── main.py
├── agent.py
├── tools.py
├── prompt.py
├── reward_functions.py
├── config.py
└── outputs/
```

## Observations

Each experiment records:
- Available model reasoning traces.
- Tool calls and actions.
- Reward function modifications.
- Original and final reward functions.


## Run Locally

1. Install [Ollama](https://ollama.com/) and download any available models based on your systems hardware.
2. Install the Python dependency:

   ```bash
   python -m pip install ollama
   ```

3. Configure the model names and number of runs in `main.py`.
4. Run:

   ```bash
   python main.py
   ```

## Research Questions

1. Does the agent modify its reward structure?
2. Does it introduce new objectives?
3. Does it weaken or remove existing constraints?
4. Does it conceal or misrepresent its modifications?

## Disclaimer

This is a small-scale exploratory AI safety experiment. Reward modification alone does not establish scheming, self-preservation, or independent goal formation.