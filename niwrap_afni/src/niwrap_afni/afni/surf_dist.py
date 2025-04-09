# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SURF_DIST_METADATA = Metadata(
    id="1440f0671a85a23be73cba7aba7157807f5c4c6f.boutiques",
    name="SurfDist",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


SurfDistParameters = typing.TypedDict('SurfDistParameters', {
    "__STYX_TYPE__": typing.Literal["SurfDist"],
    "surface": InputPathType,
    "nodepairs": InputPathType,
    "node_path_do": typing.NotRequired[str | None],
    "euclidean": bool,
    "euclidian": bool,
    "graph": bool,
    "from_node": typing.NotRequired[str | None],
    "to_nodes": typing.NotRequired[InputPathType | None],
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
        "SurfDist": surf_dist_cargs,
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
        "SurfDist": surf_dist_outputs,
    }.get(t)


class SurfDistOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surf_dist(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    distances: OutputPathType
    """File containing the distances between nodes"""


def surf_dist_params(
    surface: InputPathType,
    nodepairs: InputPathType,
    node_path_do: str | None = None,
    euclidean: bool = False,
    euclidian: bool = False,
    graph: bool = False,
    from_node: str | None = None,
    to_nodes: InputPathType | None = None,
) -> SurfDistParameters:
    """
    Build parameters.
    
    Args:
        surface: Surface on which distances are computed.
        nodepairs: Specify node pairs for distance computation.
        node_path_do: Output the shortest path between each node pair as a SUMA\
            Displayable object.
        euclidean: Calculate Euclidean distance, rather than graph distance.
        euclidian: Synonym for '-Euclidean'.
        graph: Calculate distance along the mesh (default).
        from_node: Specify one starting node for pair calculation.
        to_nodes: Specify nodes used for pair calculation when using\
            -from_node.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "SurfDist",
        "surface": surface,
        "nodepairs": nodepairs,
        "euclidean": euclidean,
        "euclidian": euclidian,
        "graph": graph,
    }
    if node_path_do is not None:
        params["node_path_do"] = node_path_do
    if from_node is not None:
        params["from_node"] = from_node
    if to_nodes is not None:
        params["to_nodes"] = to_nodes
    return params


def surf_dist_cargs(
    params: SurfDistParameters,
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
    cargs.append("SurfDist")
    cargs.append(execution.input_file(params.get("surface")))
    cargs.append(execution.input_file(params.get("nodepairs")))
    if params.get("node_path_do") is not None:
        cargs.extend([
            "-node_path_do",
            params.get("node_path_do")
        ])
    if params.get("euclidean"):
        cargs.append("-Euclidean")
    if params.get("euclidian"):
        cargs.append("-Euclidian")
    if params.get("graph"):
        cargs.append("-graph")
    if params.get("from_node") is not None:
        cargs.extend([
            "-from_node",
            params.get("from_node")
        ])
    if params.get("to_nodes") is not None:
        cargs.extend([
            "-input",
            execution.input_file(params.get("to_nodes"))
        ])
    return cargs


def surf_dist_outputs(
    params: SurfDistParameters,
    execution: Execution,
) -> SurfDistOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SurfDistOutputs(
        root=execution.output_file("."),
        distances=execution.output_file("example.1D"),
    )
    return ret


def surf_dist_execute(
    params: SurfDistParameters,
    execution: Execution,
) -> SurfDistOutputs:
    """
    Calculate shortest distance between node pairs on a surface mesh.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SurfDistOutputs`).
    """
    params = execution.params(params)
    cargs = surf_dist_cargs(params, execution)
    ret = surf_dist_outputs(params, execution)
    execution.run(cargs)
    return ret


def surf_dist(
    surface: InputPathType,
    nodepairs: InputPathType,
    node_path_do: str | None = None,
    euclidean: bool = False,
    euclidian: bool = False,
    graph: bool = False,
    from_node: str | None = None,
    to_nodes: InputPathType | None = None,
    runner: Runner | None = None,
) -> SurfDistOutputs:
    """
    Calculate shortest distance between node pairs on a surface mesh.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        surface: Surface on which distances are computed.
        nodepairs: Specify node pairs for distance computation.
        node_path_do: Output the shortest path between each node pair as a SUMA\
            Displayable object.
        euclidean: Calculate Euclidean distance, rather than graph distance.
        euclidian: Synonym for '-Euclidean'.
        graph: Calculate distance along the mesh (default).
        from_node: Specify one starting node for pair calculation.
        to_nodes: Specify nodes used for pair calculation when using\
            -from_node.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfDistOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURF_DIST_METADATA)
    params = surf_dist_params(
        surface=surface,
        nodepairs=nodepairs,
        node_path_do=node_path_do,
        euclidean=euclidean,
        euclidian=euclidian,
        graph=graph,
        from_node=from_node,
        to_nodes=to_nodes,
    )
    return surf_dist_execute(params, execution)


__all__ = [
    "SURF_DIST_METADATA",
    "SurfDistOutputs",
    "SurfDistParameters",
    "surf_dist",
    "surf_dist_params",
]
