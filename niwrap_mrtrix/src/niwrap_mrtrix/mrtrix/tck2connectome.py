# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

TCK2CONNECTOME_METADATA = Metadata(
    id="738d3835f7defdf440eba97b62da7245751874db.boutiques",
    name="tck2connectome",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


Tck2connectomeConfigParameters = typing.TypedDict('Tck2connectomeConfigParameters', {
    "__STYXTYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


Tck2connectomeParameters = typing.TypedDict('Tck2connectomeParameters', {
    "__STYXTYPE__": typing.Literal["tck2connectome"],
    "assignment_end_voxels": bool,
    "assignment_radial_search": typing.NotRequired[float | None],
    "assignment_reverse_search": typing.NotRequired[float | None],
    "assignment_forward_search": typing.NotRequired[float | None],
    "assignment_all_voxels": bool,
    "scale_length": bool,
    "scale_invlength": bool,
    "scale_invnodevol": bool,
    "scale_file": typing.NotRequired[InputPathType | None],
    "symmetric": bool,
    "zero_diagonal": bool,
    "stat_edge": typing.NotRequired[str | None],
    "tck_weights_in": typing.NotRequired[InputPathType | None],
    "keep_unassigned": bool,
    "out_assignments": typing.NotRequired[str | None],
    "vector": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Tck2connectomeConfigParameters] | None],
    "help": bool,
    "version": bool,
    "tracks_in": InputPathType,
    "nodes_in": InputPathType,
    "connectome_out": str,
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
        "tck2connectome": tck2connectome_cargs,
        "config": tck2connectome_config_cargs,
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
        "tck2connectome": tck2connectome_outputs,
    }.get(t)


def tck2connectome_config_params(
    key: str,
    value: str,
) -> Tck2connectomeConfigParameters:
    """
    Build parameters.
    
    Args:
        key: temporarily set the value of an MRtrix config file entry.
        value: temporarily set the value of an MRtrix config file entry.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "config",
        "key": key,
        "value": value,
    }
    return params


def tck2connectome_config_cargs(
    params: Tck2connectomeConfigParameters,
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
    cargs.append("-config")
    cargs.append(params.get("key"))
    cargs.append(params.get("value"))
    return cargs


class Tck2connectomeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tck2connectome(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    connectome_out: OutputPathType
    """the output .csv file containing edge weights"""
    out_assignments: OutputPathType | None
    """output the node assignments of each streamline to a file; this can be
    used subsequently e.g. by the command connectome2tck """


def tck2connectome_params(
    tracks_in: InputPathType,
    nodes_in: InputPathType,
    connectome_out: str,
    assignment_end_voxels: bool = False,
    assignment_radial_search: float | None = None,
    assignment_reverse_search: float | None = None,
    assignment_forward_search: float | None = None,
    assignment_all_voxels: bool = False,
    scale_length: bool = False,
    scale_invlength: bool = False,
    scale_invnodevol: bool = False,
    scale_file: InputPathType | None = None,
    symmetric: bool = False,
    zero_diagonal: bool = False,
    stat_edge: str | None = None,
    tck_weights_in: InputPathType | None = None,
    keep_unassigned: bool = False,
    out_assignments: str | None = None,
    vector: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Tck2connectomeConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Tck2connectomeParameters:
    """
    Build parameters.
    
    Args:
        tracks_in: the input track file.
        nodes_in: the input node parcellation image.
        connectome_out: the output .csv file containing edge weights.
        assignment_end_voxels: use a simple voxel lookup value at each\
            streamline endpoint.
        assignment_radial_search: perform a radial search from each streamline\
            endpoint to locate the nearest node. Argument is the maximum radius in\
            mm; if no node is found within this radius, the streamline endpoint is\
            not assigned to any node. Default search distance is 4mm.
        assignment_reverse_search: traverse from each streamline endpoint\
            inwards along the streamline, in search of the last node traversed by\
            the streamline. Argument is the maximum traversal length in mm (set to\
            0 to allow search to continue to the streamline midpoint).
        assignment_forward_search: project the streamline forwards from the\
            endpoint in search of a parcellation node voxel. Argument is the\
            maximum traversal length in mm.
        assignment_all_voxels: assign the streamline to all nodes it intersects\
            along its length (note that this means a streamline may be assigned to\
            more than two nodes, or indeed none at all).
        scale_length: scale each contribution to the connectome edge by the\
            length of the streamline.
        scale_invlength: scale each contribution to the connectome edge by the\
            inverse of the streamline length.
        scale_invnodevol: scale each contribution to the connectome edge by the\
            inverse of the two node volumes.
        scale_file: scale each contribution to the connectome edge according to\
            the values in a vector file.
        symmetric: Make matrices symmetric on output.
        zero_diagonal: Set matrix diagonal to zero on output.
        stat_edge: statistic for combining the values from all streamlines in\
            an edge into a single scale value for that edge (options are:\
            sum,mean,min,max; default=sum).
        tck_weights_in: specify a text scalar file containing the streamline\
            weights.
        keep_unassigned: By default, the program discards the information\
            regarding those streamlines that are not successfully assigned to a\
            node pair. Set this option to keep these values (will be the first\
            row/column in the output matrix).
        out_assignments: output the node assignments of each streamline to a\
            file; this can be used subsequently e.g. by the command connectome2tck.
        vector: output a vector representing connectivities from a given seed\
            point to target nodes, rather than a matrix of node-node connectivities.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "tck2connectome",
        "assignment_end_voxels": assignment_end_voxels,
        "assignment_all_voxels": assignment_all_voxels,
        "scale_length": scale_length,
        "scale_invlength": scale_invlength,
        "scale_invnodevol": scale_invnodevol,
        "symmetric": symmetric,
        "zero_diagonal": zero_diagonal,
        "keep_unassigned": keep_unassigned,
        "vector": vector,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "tracks_in": tracks_in,
        "nodes_in": nodes_in,
        "connectome_out": connectome_out,
    }
    if assignment_radial_search is not None:
        params["assignment_radial_search"] = assignment_radial_search
    if assignment_reverse_search is not None:
        params["assignment_reverse_search"] = assignment_reverse_search
    if assignment_forward_search is not None:
        params["assignment_forward_search"] = assignment_forward_search
    if scale_file is not None:
        params["scale_file"] = scale_file
    if stat_edge is not None:
        params["stat_edge"] = stat_edge
    if tck_weights_in is not None:
        params["tck_weights_in"] = tck_weights_in
    if out_assignments is not None:
        params["out_assignments"] = out_assignments
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def tck2connectome_cargs(
    params: Tck2connectomeParameters,
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
    cargs.append("tck2connectome")
    if params.get("assignment_end_voxels"):
        cargs.append("-assignment_end_voxels")
    if params.get("assignment_radial_search") is not None:
        cargs.extend([
            "-assignment_radial_search",
            str(params.get("assignment_radial_search"))
        ])
    if params.get("assignment_reverse_search") is not None:
        cargs.extend([
            "-assignment_reverse_search",
            str(params.get("assignment_reverse_search"))
        ])
    if params.get("assignment_forward_search") is not None:
        cargs.extend([
            "-assignment_forward_search",
            str(params.get("assignment_forward_search"))
        ])
    if params.get("assignment_all_voxels"):
        cargs.append("-assignment_all_voxels")
    if params.get("scale_length"):
        cargs.append("-scale_length")
    if params.get("scale_invlength"):
        cargs.append("-scale_invlength")
    if params.get("scale_invnodevol"):
        cargs.append("-scale_invnodevol")
    if params.get("scale_file") is not None:
        cargs.extend([
            "-scale_file",
            execution.input_file(params.get("scale_file"))
        ])
    if params.get("symmetric"):
        cargs.append("-symmetric")
    if params.get("zero_diagonal"):
        cargs.append("-zero_diagonal")
    if params.get("stat_edge") is not None:
        cargs.extend([
            "-stat_edge",
            params.get("stat_edge")
        ])
    if params.get("tck_weights_in") is not None:
        cargs.extend([
            "-tck_weights_in",
            execution.input_file(params.get("tck_weights_in"))
        ])
    if params.get("keep_unassigned"):
        cargs.append("-keep_unassigned")
    if params.get("out_assignments") is not None:
        cargs.extend([
            "-out_assignments",
            params.get("out_assignments")
        ])
    if params.get("vector"):
        cargs.append("-vector")
    if params.get("info"):
        cargs.append("-info")
    if params.get("quiet"):
        cargs.append("-quiet")
    if params.get("debug"):
        cargs.append("-debug")
    if params.get("force"):
        cargs.append("-force")
    if params.get("nthreads") is not None:
        cargs.extend([
            "-nthreads",
            str(params.get("nthreads"))
        ])
    if params.get("config") is not None:
        cargs.extend([a for c in [dyn_cargs(s["__STYXTYPE__"])(s, execution) for s in params.get("config")] for a in c])
    if params.get("help"):
        cargs.append("-help")
    if params.get("version"):
        cargs.append("-version")
    cargs.append(execution.input_file(params.get("tracks_in")))
    cargs.append(execution.input_file(params.get("nodes_in")))
    cargs.append(params.get("connectome_out"))
    return cargs


def tck2connectome_outputs(
    params: Tck2connectomeParameters,
    execution: Execution,
) -> Tck2connectomeOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Tck2connectomeOutputs(
        root=execution.output_file("."),
        connectome_out=execution.output_file(params.get("connectome_out")),
        out_assignments=execution.output_file(params.get("out_assignments")) if (params.get("out_assignments") is not None) else None,
    )
    return ret


def tck2connectome_execute(
    params: Tck2connectomeParameters,
    execution: Execution,
) -> Tck2connectomeOutputs:
    """
    Generate a connectome matrix from a streamlines file and a node parcellation
    image.
    
    
    
    References:
    
    If using the default streamline-parcel assignment mechanism (or
    -assignment_radial_search option): Smith, R. E.; Tournier, J.-D.; Calamante,
    F. & Connelly, A. The effects of SIFT on the reproducibility and biological
    accuracy of the structural connectome. NeuroImage, 2015, 104, 253-265
    
    If using -scale_invlength or -scale_invnodevol options: Hagmann, P.;
    Cammoun, L.; Gigandet, X.; Meuli, R.; Honey, C.; Wedeen, V. & Sporns, O.
    Mapping the Structural Core of Human Cerebral Cortex. PLoS Biology 6(7),
    e159.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Tck2connectomeOutputs`).
    """
    params = execution.params(params)
    cargs = tck2connectome_cargs(params, execution)
    ret = tck2connectome_outputs(params, execution)
    execution.run(cargs)
    return ret


def tck2connectome(
    tracks_in: InputPathType,
    nodes_in: InputPathType,
    connectome_out: str,
    assignment_end_voxels: bool = False,
    assignment_radial_search: float | None = None,
    assignment_reverse_search: float | None = None,
    assignment_forward_search: float | None = None,
    assignment_all_voxels: bool = False,
    scale_length: bool = False,
    scale_invlength: bool = False,
    scale_invnodevol: bool = False,
    scale_file: InputPathType | None = None,
    symmetric: bool = False,
    zero_diagonal: bool = False,
    stat_edge: str | None = None,
    tck_weights_in: InputPathType | None = None,
    keep_unassigned: bool = False,
    out_assignments: str | None = None,
    vector: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Tck2connectomeConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Tck2connectomeOutputs:
    """
    Generate a connectome matrix from a streamlines file and a node parcellation
    image.
    
    
    
    References:
    
    If using the default streamline-parcel assignment mechanism (or
    -assignment_radial_search option): Smith, R. E.; Tournier, J.-D.; Calamante,
    F. & Connelly, A. The effects of SIFT on the reproducibility and biological
    accuracy of the structural connectome. NeuroImage, 2015, 104, 253-265
    
    If using -scale_invlength or -scale_invnodevol options: Hagmann, P.;
    Cammoun, L.; Gigandet, X.; Meuli, R.; Honey, C.; Wedeen, V. & Sporns, O.
    Mapping the Structural Core of Human Cerebral Cortex. PLoS Biology 6(7),
    e159.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        tracks_in: the input track file.
        nodes_in: the input node parcellation image.
        connectome_out: the output .csv file containing edge weights.
        assignment_end_voxels: use a simple voxel lookup value at each\
            streamline endpoint.
        assignment_radial_search: perform a radial search from each streamline\
            endpoint to locate the nearest node. Argument is the maximum radius in\
            mm; if no node is found within this radius, the streamline endpoint is\
            not assigned to any node. Default search distance is 4mm.
        assignment_reverse_search: traverse from each streamline endpoint\
            inwards along the streamline, in search of the last node traversed by\
            the streamline. Argument is the maximum traversal length in mm (set to\
            0 to allow search to continue to the streamline midpoint).
        assignment_forward_search: project the streamline forwards from the\
            endpoint in search of a parcellation node voxel. Argument is the\
            maximum traversal length in mm.
        assignment_all_voxels: assign the streamline to all nodes it intersects\
            along its length (note that this means a streamline may be assigned to\
            more than two nodes, or indeed none at all).
        scale_length: scale each contribution to the connectome edge by the\
            length of the streamline.
        scale_invlength: scale each contribution to the connectome edge by the\
            inverse of the streamline length.
        scale_invnodevol: scale each contribution to the connectome edge by the\
            inverse of the two node volumes.
        scale_file: scale each contribution to the connectome edge according to\
            the values in a vector file.
        symmetric: Make matrices symmetric on output.
        zero_diagonal: Set matrix diagonal to zero on output.
        stat_edge: statistic for combining the values from all streamlines in\
            an edge into a single scale value for that edge (options are:\
            sum,mean,min,max; default=sum).
        tck_weights_in: specify a text scalar file containing the streamline\
            weights.
        keep_unassigned: By default, the program discards the information\
            regarding those streamlines that are not successfully assigned to a\
            node pair. Set this option to keep these values (will be the first\
            row/column in the output matrix).
        out_assignments: output the node assignments of each streamline to a\
            file; this can be used subsequently e.g. by the command connectome2tck.
        vector: output a vector representing connectivities from a given seed\
            point to target nodes, rather than a matrix of node-node connectivities.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Tck2connectomeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCK2CONNECTOME_METADATA)
    params = tck2connectome_params(
        assignment_end_voxels=assignment_end_voxels,
        assignment_radial_search=assignment_radial_search,
        assignment_reverse_search=assignment_reverse_search,
        assignment_forward_search=assignment_forward_search,
        assignment_all_voxels=assignment_all_voxels,
        scale_length=scale_length,
        scale_invlength=scale_invlength,
        scale_invnodevol=scale_invnodevol,
        scale_file=scale_file,
        symmetric=symmetric,
        zero_diagonal=zero_diagonal,
        stat_edge=stat_edge,
        tck_weights_in=tck_weights_in,
        keep_unassigned=keep_unassigned,
        out_assignments=out_assignments,
        vector=vector,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        tracks_in=tracks_in,
        nodes_in=nodes_in,
        connectome_out=connectome_out,
    )
    return tck2connectome_execute(params, execution)


__all__ = [
    "TCK2CONNECTOME_METADATA",
    "Tck2connectomeConfigParameters",
    "Tck2connectomeOutputs",
    "Tck2connectomeParameters",
    "tck2connectome",
    "tck2connectome_config_params",
    "tck2connectome_params",
]
