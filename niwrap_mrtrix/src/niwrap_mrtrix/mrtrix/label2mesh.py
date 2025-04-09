# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

LABEL2MESH_METADATA = Metadata(
    id="cdcb0167501c7277846754252872bdd4aafe4ee0.boutiques",
    name="label2mesh",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


Label2meshConfigParameters = typing.TypedDict('Label2meshConfigParameters', {
    "__STYX_TYPE__": typing.Literal["config"],
    "key": str,
    "value": str,
})


Label2meshParameters = typing.TypedDict('Label2meshParameters', {
    "__STYX_TYPE__": typing.Literal["label2mesh"],
    "blocky": bool,
    "info": bool,
    "quiet": bool,
    "debug": bool,
    "force": bool,
    "nthreads": typing.NotRequired[int | None],
    "config": typing.NotRequired[list[Label2meshConfigParameters] | None],
    "help": bool,
    "version": bool,
    "nodes_in": InputPathType,
    "mesh_out": str,
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
        "label2mesh": label2mesh_cargs,
        "config": label2mesh_config_cargs,
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
        "label2mesh": label2mesh_outputs,
    }.get(t)


def label2mesh_config_params(
    key: str,
    value: str,
) -> Label2meshConfigParameters:
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


def label2mesh_config_cargs(
    params: Label2meshConfigParameters,
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


class Label2meshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label2mesh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mesh_out: OutputPathType
    """the output mesh file"""


def label2mesh_params(
    nodes_in: InputPathType,
    mesh_out: str,
    blocky: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Label2meshConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
) -> Label2meshParameters:
    """
    Build parameters.
    
    Args:
        nodes_in: the input node parcellation image.
        mesh_out: the output mesh file.
        blocky: generate 'blocky' meshes with precise delineation of voxel\
            edges, rather than the default Marching Cubes approach.
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
        "__STYXTYPE__": "label2mesh",
        "blocky": blocky,
        "info": info,
        "quiet": quiet,
        "debug": debug,
        "force": force,
        "help": help_,
        "version": version,
        "nodes_in": nodes_in,
        "mesh_out": mesh_out,
    }
    if nthreads is not None:
        params["nthreads"] = nthreads
    if config is not None:
        params["config"] = config
    return params


def label2mesh_cargs(
    params: Label2meshParameters,
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
    cargs.append("label2mesh")
    if params.get("blocky"):
        cargs.append("-blocky")
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
    cargs.append(execution.input_file(params.get("nodes_in")))
    cargs.append(params.get("mesh_out"))
    return cargs


def label2mesh_outputs(
    params: Label2meshParameters,
    execution: Execution,
) -> Label2meshOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = Label2meshOutputs(
        root=execution.output_file("."),
        mesh_out=execution.output_file(params.get("mesh_out")),
    )
    return ret


def label2mesh_execute(
    params: Label2meshParameters,
    execution: Execution,
) -> Label2meshOutputs:
    """
    Generate meshes from a label image.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `Label2meshOutputs`).
    """
    params = execution.params(params)
    cargs = label2mesh_cargs(params, execution)
    ret = label2mesh_outputs(params, execution)
    execution.run(cargs)
    return ret


def label2mesh(
    nodes_in: InputPathType,
    mesh_out: str,
    blocky: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Label2meshConfigParameters] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Label2meshOutputs:
    """
    Generate meshes from a label image.
    
    
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        nodes_in: the input node parcellation image.
        mesh_out: the output mesh file.
        blocky: generate 'blocky' meshes with precise delineation of voxel\
            edges, rather than the default Marching Cubes approach.
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
        NamedTuple of outputs (described in `Label2meshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL2MESH_METADATA)
    params = label2mesh_params(
        blocky=blocky,
        info=info,
        quiet=quiet,
        debug=debug,
        force=force,
        nthreads=nthreads,
        config=config,
        help_=help_,
        version=version,
        nodes_in=nodes_in,
        mesh_out=mesh_out,
    )
    return label2mesh_execute(params, execution)


__all__ = [
    "LABEL2MESH_METADATA",
    "Label2meshConfigParameters",
    "Label2meshOutputs",
    "Label2meshParameters",
    "label2mesh",
    "label2mesh_config_params",
    "label2mesh_params",
]
