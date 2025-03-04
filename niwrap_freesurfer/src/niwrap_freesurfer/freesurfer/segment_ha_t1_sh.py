# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

SEGMENT_HA_T1_SH_METADATA = Metadata(
    id="33c1985d7e603bd0c84961ad260a84289d2bd93f.boutiques",
    name="segmentHA_T1.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


SegmentHaT1ShParameters = typing.TypedDict('SegmentHaT1ShParameters', {
    "__STYX_TYPE__": typing.Literal["segmentHA_T1.sh"],
    "input_image": InputPathType,
    "output_directory": str,
    "brain_mask": typing.NotRequired[InputPathType | None],
    "verbose": bool,
    "debug": bool,
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
        "segmentHA_T1.sh": segment_ha_t1_sh_cargs,
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
        "segmentHA_T1.sh": segment_ha_t1_sh_outputs,
    }.get(t)


class SegmentHaT1ShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `segment_ha_t1_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    hippocampus_aseg: OutputPathType
    """Segmented hippocampal subfields."""
    amygdala_aseg: OutputPathType
    """Segmented amygdalar subfields."""


def segment_ha_t1_sh_params(
    input_image: InputPathType,
    output_directory: str,
    brain_mask: InputPathType | None = None,
    verbose: bool = False,
    debug: bool = False,
) -> SegmentHaT1ShParameters:
    """
    Build parameters.
    
    Args:
        input_image: The input T1-weighted MRI image for hippocampal/amygdalar\
            segmentation.
        output_directory: The directory where the output will be saved.
        brain_mask: Use a specific brain mask for segmentation.
        verbose: Increase the verbosity of the output.
        debug: Enable debugging mode.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "segmentHA_T1.sh",
        "input_image": input_image,
        "output_directory": output_directory,
        "verbose": verbose,
        "debug": debug,
    }
    if brain_mask is not None:
        params["brain_mask"] = brain_mask
    return params


def segment_ha_t1_sh_cargs(
    params: SegmentHaT1ShParameters,
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
    cargs.append("segmentHA_T1.sh")
    cargs.append(execution.input_file(params.get("input_image")))
    cargs.append(params.get("output_directory"))
    if params.get("brain_mask") is not None:
        cargs.extend([
            "--brainmask",
            execution.input_file(params.get("brain_mask"))
        ])
    if params.get("verbose"):
        cargs.append("--verbose")
    if params.get("debug"):
        cargs.append("--debug")
    return cargs


def segment_ha_t1_sh_outputs(
    params: SegmentHaT1ShParameters,
    execution: Execution,
) -> SegmentHaT1ShOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = SegmentHaT1ShOutputs(
        root=execution.output_file("."),
        hippocampus_aseg=execution.output_file(params.get("output_directory") + "/hippocampus_aseg.mgz"),
        amygdala_aseg=execution.output_file(params.get("output_directory") + "/amygdala_aseg.mgz"),
    )
    return ret


def segment_ha_t1_sh_execute(
    params: SegmentHaT1ShParameters,
    execution: Execution,
) -> SegmentHaT1ShOutputs:
    """
    Tool for hippocampal/amygdalar subfield segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `SegmentHaT1ShOutputs`).
    """
    params = execution.params(params)
    cargs = segment_ha_t1_sh_cargs(params, execution)
    ret = segment_ha_t1_sh_outputs(params, execution)
    execution.run(cargs)
    return ret


def segment_ha_t1_sh(
    input_image: InputPathType,
    output_directory: str,
    brain_mask: InputPathType | None = None,
    verbose: bool = False,
    debug: bool = False,
    runner: Runner | None = None,
) -> SegmentHaT1ShOutputs:
    """
    Tool for hippocampal/amygdalar subfield segmentation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: The input T1-weighted MRI image for hippocampal/amygdalar\
            segmentation.
        output_directory: The directory where the output will be saved.
        brain_mask: Use a specific brain mask for segmentation.
        verbose: Increase the verbosity of the output.
        debug: Enable debugging mode.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SegmentHaT1ShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SEGMENT_HA_T1_SH_METADATA)
    params = segment_ha_t1_sh_params(
        input_image=input_image,
        output_directory=output_directory,
        brain_mask=brain_mask,
        verbose=verbose,
        debug=debug,
    )
    return segment_ha_t1_sh_execute(params, execution)


__all__ = [
    "SEGMENT_HA_T1_SH_METADATA",
    "SegmentHaT1ShOutputs",
    "SegmentHaT1ShParameters",
    "segment_ha_t1_sh",
    "segment_ha_t1_sh_params",
]
