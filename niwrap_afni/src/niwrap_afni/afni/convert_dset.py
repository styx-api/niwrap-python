# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

CONVERT_DSET_METADATA = Metadata(
    id="4beee4c1c48b313053c056b039eaf7a92a5a5c03.boutiques",
    name="ConvertDset",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


ConvertDsetParameters = typing.TypedDict('ConvertDsetParameters', {
    "__STYXTYPE__": typing.Literal["ConvertDset"],
    "output_type": list[typing.Literal["niml_asc", "niml_bi", "1D", "1Dp", "1Dpt", "gii", "gii_asc", "gii_b64", "gii_b64gz", "1D_stderr", "1D_stdout", "niml_stderr", "niml_stdout", "1Dp_stdout", "1Dp_stderr", "1Dpt_stdout", "1Dpt_stderr"]],
    "input_dataset": InputPathType,
    "input_type": typing.NotRequired[typing.Literal["niml", "1D", "dx"] | None],
    "output_prefix": typing.NotRequired[str | None],
    "dset_labels": typing.NotRequired[str | None],
    "add_node_index": bool,
    "node_index_file": typing.NotRequired[InputPathType | None],
    "node_select_file": typing.NotRequired[InputPathType | None],
    "prepend_node_index": bool,
    "pad_to_node": typing.NotRequired[str | None],
    "labelize": typing.NotRequired[InputPathType | None],
    "graphize": bool,
    "graph_nodelist": typing.NotRequired[str | None],
    "graph_full_nodelist": typing.NotRequired[InputPathType | None],
    "graph_named_nodelist": typing.NotRequired[str | None],
    "graph_xyz_lpi": bool,
    "graph_edgelist": typing.NotRequired[InputPathType | None],
    "onegraph": bool,
    "multigraph": bool,
    "split": typing.NotRequired[int | None],
    "no_history": bool,
})


def dyn_cargs(
    t: str,
) -> typing.Any:
    """
    Get build cargs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build cargs function.
    """
    return {
        "ConvertDset": convert_dset_cargs,
    }.get(t)


def dyn_outputs(
    t: str,
) -> typing.Any:
    """
    Get build outputs function by command type.
    
    Args:
        t: Command type.
    Returns:
        Build outputs function.
    """
    return {
        "ConvertDset": convert_dset_outputs,
    }.get(t)


class ConvertDsetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_dset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    converted_dataset: OutputPathType | None
    """Converted dataset output"""


def convert_dset_params(
    output_type: list[typing.Literal["niml_asc", "niml_bi", "1D", "1Dp", "1Dpt", "gii", "gii_asc", "gii_b64", "gii_b64gz", "1D_stderr", "1D_stdout", "niml_stderr", "niml_stdout", "1Dp_stdout", "1Dp_stderr", "1Dpt_stdout", "1Dpt_stderr"]],
    input_dataset: InputPathType,
    input_type: typing.Literal["niml", "1D", "dx"] | None = None,
    output_prefix: str | None = None,
    dset_labels: str | None = None,
    add_node_index: bool = False,
    node_index_file: InputPathType | None = None,
    node_select_file: InputPathType | None = None,
    prepend_node_index: bool = False,
    pad_to_node: str | None = None,
    labelize: InputPathType | None = None,
    graphize: bool = False,
    graph_nodelist: str | None = None,
    graph_full_nodelist: InputPathType | None = None,
    graph_named_nodelist: str | None = None,
    graph_xyz_lpi: bool = False,
    graph_edgelist: InputPathType | None = None,
    onegraph: bool = False,
    multigraph: bool = False,
    split: int | None = None,
    no_history: bool = False,
) -> ConvertDsetParameters:
    """
    Build parameters.
    
    Args:
        output_type: Type of output datasets.
        input_dataset: Input dataset to be converted.
        input_type: Type of input datasets.
        output_prefix: Output prefix for dataset.
        dset_labels: Label the columns (sub-bricks) of the output dataset.
        add_node_index: Add a node index element if one does not exist in the\
            input dataset.
        node_index_file: File containing node indices.
        node_select_file: File specifying the nodes to keep in the output.
        prepend_node_index: Add a node index column to the data.
        pad_to_node: Output a full dataset from node 0 to MAX_INDEX.
        labelize: Turn the dataset into a labeled set per the colormap in CMAP.
        graphize: Turn the dataset into a SUMA graph dataset.
        graph_nodelist: Two files specifying the indices and the coordinates of\
            the graph's nodes.
        graph_full_nodelist: Similar to -graph_nodelist_1D but without need for\
            NODEINDLIST.1D.
        graph_named_nodelist: Two files specifying graph node indices, string\
            labels, and their coordinates.
        graph_xyz_lpi: Coordinates in NodeList.1D are in LPI instead of RAI.
        graph_edgelist: Indices of graph nodes defining edge.
        onegraph: Expect input dataset to be one square matrix defining the\
            graph (default).
        multigraph: Expect each column in input dataset to define an entire\
            graph.
        split: Split a multi-column dataset into about N output datasets.
        no_history: Do not include a history element in the output.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "ConvertDset",
        "output_type": output_type,
        "input_dataset": input_dataset,
        "add_node_index": add_node_index,
        "prepend_node_index": prepend_node_index,
        "graphize": graphize,
        "graph_xyz_lpi": graph_xyz_lpi,
        "onegraph": onegraph,
        "multigraph": multigraph,
        "no_history": no_history,
    }
    if input_type is not None:
        params["input_type"] = input_type
    if output_prefix is not None:
        params["output_prefix"] = output_prefix
    if dset_labels is not None:
        params["dset_labels"] = dset_labels
    if node_index_file is not None:
        params["node_index_file"] = node_index_file
    if node_select_file is not None:
        params["node_select_file"] = node_select_file
    if pad_to_node is not None:
        params["pad_to_node"] = pad_to_node
    if labelize is not None:
        params["labelize"] = labelize
    if graph_nodelist is not None:
        params["graph_nodelist"] = graph_nodelist
    if graph_full_nodelist is not None:
        params["graph_full_nodelist"] = graph_full_nodelist
    if graph_named_nodelist is not None:
        params["graph_named_nodelist"] = graph_named_nodelist
    if graph_edgelist is not None:
        params["graph_edgelist"] = graph_edgelist
    if split is not None:
        params["split"] = split
    return params


def convert_dset_cargs(
    params: ConvertDsetParameters,
    execution: Execution,
) -> list[str]:
    """
    Build command-line arguments from parameters.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Command-line arguments.
    """
    cargs = []
    cargs.append("ConvertDset")
    cargs.extend([
        "-o_",
        *params.get("output_type")
    ])
    cargs.extend([
        "-input",
        execution.input_file(params.get("input_dataset"))
    ])
    if params.get("input_type") is not None:
        cargs.extend([
            "-i_",
            params.get("input_type")
        ])
    if params.get("output_prefix") is not None:
        cargs.extend([
            "-prefix",
            params.get("output_prefix")
        ])
    if params.get("dset_labels") is not None:
        cargs.extend([
            "-dset_labels",
            params.get("dset_labels")
        ])
    if params.get("add_node_index"):
        cargs.append("-add_node_index")
    if params.get("node_index_file") is not None:
        cargs.extend([
            "-node_index_1D",
            execution.input_file(params.get("node_index_file"))
        ])
    if params.get("node_select_file") is not None:
        cargs.extend([
            "-node_select_1D",
            execution.input_file(params.get("node_select_file"))
        ])
    if params.get("prepend_node_index"):
        cargs.append("-prepend_node_index_1D")
    if params.get("pad_to_node") is not None:
        cargs.extend([
            "-pad_to_node",
            params.get("pad_to_node")
        ])
    if params.get("labelize") is not None:
        cargs.extend([
            "-labelize",
            execution.input_file(params.get("labelize"))
        ])
    if params.get("graphize"):
        cargs.append("-graphize")
    if params.get("graph_nodelist") is not None:
        cargs.extend([
            "-graph_nodelist_1D",
            params.get("graph_nodelist")
        ])
    if params.get("graph_full_nodelist") is not None:
        cargs.extend([
            "-graph_full_nodelist_1D",
            execution.input_file(params.get("graph_full_nodelist"))
        ])
    if params.get("graph_named_nodelist") is not None:
        cargs.extend([
            "-graph_named_nodelist_txt",
            params.get("graph_named_nodelist")
        ])
    if params.get("graph_xyz_lpi"):
        cargs.append("-graph_XYZ_LPI")
    if params.get("graph_edgelist") is not None:
        cargs.extend([
            "-graph_edgelist_1D",
            execution.input_file(params.get("graph_edgelist"))
        ])
    if params.get("onegraph"):
        cargs.append("-onegraph")
    if params.get("multigraph"):
        cargs.append("-multigraph")
    if params.get("split") is not None:
        cargs.extend([
            "-split",
            str(params.get("split"))
        ])
    if params.get("no_history"):
        cargs.append("-no_history")
    return cargs


def convert_dset_outputs(
    params: ConvertDsetParameters,
    execution: Execution,
) -> ConvertDsetOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = ConvertDsetOutputs(
        root=execution.output_file("."),
        converted_dataset=execution.output_file(params.get("output_prefix")) if (params.get("output_prefix") is not None) else None,
    )
    return ret


def convert_dset_execute(
    params: ConvertDsetParameters,
    execution: Execution,
) -> ConvertDsetOutputs:
    """
    Converts a surface dataset from one format to another.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `ConvertDsetOutputs`).
    """
    params = execution.params(params)
    cargs = convert_dset_cargs(params, execution)
    ret = convert_dset_outputs(params, execution)
    execution.run(cargs)
    return ret


def convert_dset(
    output_type: list[typing.Literal["niml_asc", "niml_bi", "1D", "1Dp", "1Dpt", "gii", "gii_asc", "gii_b64", "gii_b64gz", "1D_stderr", "1D_stdout", "niml_stderr", "niml_stdout", "1Dp_stdout", "1Dp_stderr", "1Dpt_stdout", "1Dpt_stderr"]],
    input_dataset: InputPathType,
    input_type: typing.Literal["niml", "1D", "dx"] | None = None,
    output_prefix: str | None = None,
    dset_labels: str | None = None,
    add_node_index: bool = False,
    node_index_file: InputPathType | None = None,
    node_select_file: InputPathType | None = None,
    prepend_node_index: bool = False,
    pad_to_node: str | None = None,
    labelize: InputPathType | None = None,
    graphize: bool = False,
    graph_nodelist: str | None = None,
    graph_full_nodelist: InputPathType | None = None,
    graph_named_nodelist: str | None = None,
    graph_xyz_lpi: bool = False,
    graph_edgelist: InputPathType | None = None,
    onegraph: bool = False,
    multigraph: bool = False,
    split: int | None = None,
    no_history: bool = False,
    runner: Runner | None = None,
) -> ConvertDsetOutputs:
    """
    Converts a surface dataset from one format to another.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        output_type: Type of output datasets.
        input_dataset: Input dataset to be converted.
        input_type: Type of input datasets.
        output_prefix: Output prefix for dataset.
        dset_labels: Label the columns (sub-bricks) of the output dataset.
        add_node_index: Add a node index element if one does not exist in the\
            input dataset.
        node_index_file: File containing node indices.
        node_select_file: File specifying the nodes to keep in the output.
        prepend_node_index: Add a node index column to the data.
        pad_to_node: Output a full dataset from node 0 to MAX_INDEX.
        labelize: Turn the dataset into a labeled set per the colormap in CMAP.
        graphize: Turn the dataset into a SUMA graph dataset.
        graph_nodelist: Two files specifying the indices and the coordinates of\
            the graph's nodes.
        graph_full_nodelist: Similar to -graph_nodelist_1D but without need for\
            NODEINDLIST.1D.
        graph_named_nodelist: Two files specifying graph node indices, string\
            labels, and their coordinates.
        graph_xyz_lpi: Coordinates in NodeList.1D are in LPI instead of RAI.
        graph_edgelist: Indices of graph nodes defining edge.
        onegraph: Expect input dataset to be one square matrix defining the\
            graph (default).
        multigraph: Expect each column in input dataset to define an entire\
            graph.
        split: Split a multi-column dataset into about N output datasets.
        no_history: Do not include a history element in the output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertDsetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_DSET_METADATA)
    params = convert_dset_params(
        output_type=output_type,
        input_dataset=input_dataset,
        input_type=input_type,
        output_prefix=output_prefix,
        dset_labels=dset_labels,
        add_node_index=add_node_index,
        node_index_file=node_index_file,
        node_select_file=node_select_file,
        prepend_node_index=prepend_node_index,
        pad_to_node=pad_to_node,
        labelize=labelize,
        graphize=graphize,
        graph_nodelist=graph_nodelist,
        graph_full_nodelist=graph_full_nodelist,
        graph_named_nodelist=graph_named_nodelist,
        graph_xyz_lpi=graph_xyz_lpi,
        graph_edgelist=graph_edgelist,
        onegraph=onegraph,
        multigraph=multigraph,
        split=split,
        no_history=no_history,
    )
    return convert_dset_execute(params, execution)


__all__ = [
    "CONVERT_DSET_METADATA",
    "ConvertDsetOutputs",
    "ConvertDsetParameters",
    "convert_dset",
    "convert_dset_params",
]
