from overrides import overrides

from allennlp.common.util import JsonDict
from allennlp.data import Instance
from allennlp.predictors.predictor import Predictor


@Predictor.register("contrastive")
class ContrastivePredictor(Predictor):
    """Predictor wrapper for the ContrastiveTextEncoder.

    Registered as a `Predictor` with name "contrastive".
    """

    @overrides
    def _json_to_instance(self, json_dict: JsonDict) -> Instance:
        text = json_dict["text"]
        # Context manager ensures that the sample_spans property of our DatasetReader is False
        with self._dataset_reader.no_sample():
            return self._dataset_reader.text_to_instance(text=text)
