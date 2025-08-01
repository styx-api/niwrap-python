# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRI_XVOLAVG_METADATA = Metadata(
    id="59e2b553a940c4fdb7f3dcfd7c0ee7148a4cce23.boutiques",
    name="mri_xvolavg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MriXvolavgParameters = typing.TypedDict('MriXvolavgParameters', {
    "__STYXTYPE__": typing.Literal["mri_xvolavg"],
    "input_volumes": list[InputPathType],
    "vol_type": str,
    "output_volume": str,
    "output_type": typing.NotRequired[str | None],
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
        "mri_xvolavg": mri_xvolavg_cargs,
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
        "mri_xvolavg": mri_xvolavg_outputs,
    }.get(t)


class MriXvolavgOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_xvolavg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    averaged_output: OutputPathType
    """The averaged output volume."""


def mri_xvolavg_params(
    input_volumes: list[InputPathType],
    vol_type: str,
    output_volume: str,
    output_type: str | None = None,
) -> MriXvolavgParameters:
    """
    Build parameters.
    
    Args:
        input_volumes: Path(s) to input volume(s). This option can be repeated\
            for each input volume.
        vol_type: Format type of all input volumes.
        output_volume: Path to output volume.
        output_type: Format type of the output volume (default is that of input\
            volumes).
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mri_xvolavg",
        "input_volumes": input_volumes,
        "vol_type": vol_type,
        "output_volume": output_volume,
    }
    if output_type is not None:
        params["output_type"] = output_type
    return params


def mri_xvolavg_cargs(
    params: MriXvolavgParameters,
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
    cargs.append("mri_xvolavg")
    cargs.extend([
        "--vol",
        *[execution.input_file(f) for f in params.get("input_volumes")]
    ])
    cargs.extend([
        "--vol_type",
        params.get("vol_type")
    ])
    cargs.extend([
        "--out",
        params.get("output_volume")
    ])
    if params.get("output_type") is not None:
        cargs.extend([
            "--out_type",
            params.get("output_type")
        ])
    return cargs


def mri_xvolavg_outputs(
    params: MriXvolavgParameters,
    execution: Execution,
) -> MriXvolavgOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MriXvolavgOutputs(
        root=execution.output_file("."),
        averaged_output=execution.output_file(params.get("output_volume")),
    )
    return ret


def mri_xvolavg_execute(
    params: MriXvolavgParameters,
    execution: Execution,
) -> MriXvolavgOutputs:
    """
    Tool to average multiple volumes together (including 4D volumes).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MriXvolavgOutputs`).
    """
    params = execution.params(params)
    cargs = mri_xvolavg_cargs(params, execution)
    ret = mri_xvolavg_outputs(params, execution)
    execution.run(cargs)
    return ret


def mri_xvolavg(
    input_volumes: list[InputPathType],
    vol_type: str,
    output_volume: str,
    output_type: str | None = None,
    runner: Runner | None = None,
) -> MriXvolavgOutputs:
    """
    Tool to average multiple volumes together (including 4D volumes).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volumes: Path(s) to input volume(s). This option can be repeated\
            for each input volume.
        vol_type: Format type of all input volumes.
        output_volume: Path to output volume.
        output_type: Format type of the output volume (default is that of input\
            volumes).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriXvolavgOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_XVOLAVG_METADATA)
    params = mri_xvolavg_params(
        input_volumes=input_volumes,
        vol_type=vol_type,
        output_volume=output_volume,
        output_type=output_type,
    )
    return mri_xvolavg_execute(params, execution)


__all__ = [
    "MRI_XVOLAVG_METADATA",
    "MriXvolavgOutputs",
    "MriXvolavgParameters",
    "mri_xvolavg",
    "mri_xvolavg_params",
]
