# Exercise 05 — VisualSort: Retail Image Routing with Transfer Learning

[![Open starter in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lathrahul/modern-ai-ml-exercises/blob/main/exercise-05-visual-sort/notebooks/getting_started.ipynb) [![Explore outputs in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/lathrahul/modern-ai-ml-exercises/blob/main/shared/explore_outputs_in_colab.ipynb)

**Release:** Session 11  
**Due:** Session 13 debrief  
**Expected effort:** 5–7 hours  
**Work mode:** Teams of two

## Start and submit

1. Open the starter notebook with the Colab button above and select **File → Save a copy in Drive**. Do not use a GitHub Gist.
2. Complete the analysis, restart the runtime, and run every cell from top to bottom.
3. Validate `submission.csv` and inspect the outputs with the [shared output explorer](../shared/OUTPUT_EXPLORER.md).
4. Download the executed notebook, model artifact, and required outputs to your computer.
5. Assemble the files using the [submission guidelines](../shared/submission_guidelines.md) and submit them through the Exercise 05 assignment in Blackboard. Follow the Blackboard assignment for the designated team submitter and due date.

## Your role

An online marketplace receives product images before structured catalog metadata is complete. Build a visual classifier that routes each image into one of ten coarse merchandise categories. A human catalog specialist reviews low-confidence cases.

## Data

- `data/train_images.npz`: 12,000 grayscale 28×28 product images and randomized IDs.
- `data/train_labels.csv`: category labels.
- `data/test_images.npz`: 3,000 unlabeled images.
- `data/label_map.csv`: allowed labels and class indices.

Load an archive with:

```python
archive = np.load("data/train_images.npz")
images, image_ids = archive["images"], archive["image_id"]
```

## Required analysis

1. Visualize every category and audit balance.
2. Establish a simple flattened-pixel or shallow neural-network baseline.
3. Train an MLP and document learning curves and overfitting controls.
4. Adapt a pretrained image model by resizing and converting grayscale images to three channels.
5. Compare frozen-feature and fine-tuned stages against the baseline.
6. Report macro F1, accuracy, per-class recall, confusion matrix, runtime, and model size.
7. Define a confidence-based human-review policy and analyze its coverage/error trade-off.
8. Investigate at least two recurring confusion pairs.

## Expected outputs

### Prediction file

```text
image_id,predicted_label
IMG-123456,coat
```

Validate with:

```bash
python3 checks/validate_submission.py submission.csv
```

### Model card and demo

Submit an executed Colab notebook, saved model or weights, experiment report, and a two-page model card covering intended use, data, metrics, failure modes, review threshold, and responsible-use limits. Demonstrate inference on five images.

## Technical evaluation

Macro F1 on withheld outcomes is the primary metric so each merchandise class matters equally. There is no public course leaderboard.

## Source

[Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist) by Zalando Research, MIT License.
