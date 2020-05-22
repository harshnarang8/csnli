from csnli.nmt.onmt.modules.UtilClass import LayerNorm, Elementwise
from csnli.nmt.onmt.modules.Gate import context_gate_factory, ContextGate
from csnli.nmt.onmt.modules.GlobalAttention import GlobalAttention
from csnli.nmt.onmt.modules.CopyGenerator import CopyGenerator, CopyGeneratorLossCompute
from csnli.nmt.onmt.modules.StructuredAttention import MatrixTree
from csnli.nmt.onmt.modules.Transformer import \
   TransformerEncoder, TransformerDecoder, PositionwiseFeedForward
from csnli.nmt.onmt.modules.MultiHeadedAttn import MultiHeadedAttention
from csnli.nmt.onmt.modules.StackedRNN import StackedLSTM, StackedGRU
from csnli.nmt.onmt.modules.Embeddings import Embeddings, PositionalEncoding
from csnli.nmt.onmt.modules.WeightNorm import WeightNormConv2d

from csnli.nmt.onmt.Models import EncoderBase, MeanEncoder, StdRNNDecoder, \
    RNNDecoderBase, InputFeedRNNDecoder, RNNEncoder, NMTModel

from csnli.nmt.onmt.modules.SRU import check_sru_requirement
can_use_sru = check_sru_requirement()
if can_use_sru:
    from csnli.nmt.onmt.modules.SRU import SRU


# For flake8 compatibility.
__all__ = [EncoderBase, MeanEncoder, RNNDecoderBase, InputFeedRNNDecoder,
           RNNEncoder, NMTModel,
           StdRNNDecoder, ContextGate, GlobalAttention, 
           PositionwiseFeedForward, PositionalEncoding,
           CopyGenerator, MultiHeadedAttention,
           LayerNorm,
           TransformerEncoder, TransformerDecoder, Embeddings, Elementwise,
           MatrixTree, 
           StackedLSTM, StackedGRU,
           context_gate_factory, CopyGeneratorLossCompute]

if can_use_sru:
    __all__.extend([SRU, check_sru_requirement])
