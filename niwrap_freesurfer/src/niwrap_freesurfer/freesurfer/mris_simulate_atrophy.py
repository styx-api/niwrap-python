# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *

MRIS_SIMULATE_ATROPHY_METADATA = Metadata(
    id="b2e923443b64cd119265f582a44ff716bd98c53c.boutiques",
    name="mris_simulate_atrophy",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


MrisSimulateAtrophyParameters = typing.TypedDict('MrisSimulateAtrophyParameters', {
    "__STYXTYPE__": typing.Literal["mris_simulate_atrophy"],
    "subject": str,
    "hemi": str,
    "label": str,
    "atrophy_fraction": float,
    "output_volume": str,
    "atrophy_percent": typing.NotRequired[float | None],
    "noise_level": typing.NotRequired[float | None],
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
        "mris_simulate_atrophy": mris_simulate_atrophy_cargs,
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
        "mris_simulate_atrophy": mris_simulate_atrophy_outputs,
    }.get(t)


class MrisSimulateAtrophyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_simulate_atrophy(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Atrophy simulation output volume."""


def mris_simulate_atrophy_params(
    subject: str,
    hemi: str,
    label: str,
    atrophy_fraction: float,
    output_volume: str,
    atrophy_percent: float | None = None,
    noise_level: float | None = None,
) -> MrisSimulateAtrophyParameters:
    """
    Build parameters.
    
    Args:
        subject: Subject identifier.
        hemi: Hemisphere (e.g. lh or rh).
        label: Label of the brain region.
        atrophy_fraction: Target atrophy fraction.
        output_volume: Output volume file.
        atrophy_percent: Percentage atrophy to simulate of structure.
        noise_level: Gaussian noise level to add.
    Returns:
        Parameter dictionary
    """
    params = {
        "__STYXTYPE__": "mris_simulate_atrophy",
        "subject": subject,
        "hemi": hemi,
        "label": label,
        "atrophy_fraction": atrophy_fraction,
        "output_volume": output_volume,
    }
    if atrophy_percent is not None:
        params["atrophy_percent"] = atrophy_percent
    if noise_level is not None:
        params["noise_level"] = noise_level
    return params


def mris_simulate_atrophy_cargs(
    params: MrisSimulateAtrophyParameters,
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
    cargs.append("mris_simulate_atrophy")
    cargs.append(params.get("subject"))
    cargs.append(params.get("hemi"))
    cargs.append(params.get("label"))
    cargs.append(str(params.get("atrophy_fraction")))
    cargs.append(params.get("output_volume"))
    if params.get("atrophy_percent") is not None:
        cargs.extend([
            "-a",
            str(params.get("atrophy_percent"))
        ])
    if params.get("noise_level") is not None:
        cargs.extend([
            "-n",
            str(params.get("noise_level"))
        ])
    return cargs


def mris_simulate_atrophy_outputs(
    params: MrisSimulateAtrophyParameters,
    execution: Execution,
) -> MrisSimulateAtrophyOutputs:
    """
    Build outputs object containing output file paths and possibly stdout/stderr.
    
    Args:
        params: The parameters.
        execution: The execution object for resolving input paths.
    Returns:
        Outputs object.
    """
    ret = MrisSimulateAtrophyOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(params.get("output_volume")),
    )
    return ret


def mris_simulate_atrophy_execute(
    params: MrisSimulateAtrophyParameters,
    execution: Execution,
) -> MrisSimulateAtrophyOutputs:
    """
    Simulate atrophy on brain structures.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        params: The parameters.
        execution: The execution object.
    Returns:
        NamedTuple of outputs (described in `MrisSimulateAtrophyOutputs`).
    """
    params = execution.params(params)
    cargs = mris_simulate_atrophy_cargs(params, execution)
    ret = mris_simulate_atrophy_outputs(params, execution)
    execution.run(cargs)
    return ret


def mris_simulate_atrophy(
    subject: str,
    hemi: str,
    label: str,
    atrophy_fraction: float,
    output_volume: str,
    atrophy_percent: float | None = None,
    noise_level: float | None = None,
    runner: Runner | None = None,
) -> MrisSimulateAtrophyOutputs:
    """
    Simulate atrophy on brain structures.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier.
        hemi: Hemisphere (e.g. lh or rh).
        label: Label of the brain region.
        atrophy_fraction: Target atrophy fraction.
        output_volume: Output volume file.
        atrophy_percent: Percentage atrophy to simulate of structure.
        noise_level: Gaussian noise level to add.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisSimulateAtrophyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_SIMULATE_ATROPHY_METADATA)
    params = mris_simulate_atrophy_params(
        subject=subject,
        hemi=hemi,
        label=label,
        atrophy_fraction=atrophy_fraction,
        output_volume=output_volume,
        atrophy_percent=atrophy_percent,
        noise_level=noise_level,
    )
    return mris_simulate_atrophy_execute(params, execution)


__all__ = [
    "MRIS_SIMULATE_ATROPHY_METADATA",
    "MrisSimulateAtrophyOutputs",
    "MrisSimulateAtrophyParameters",
    "mris_simulate_atrophy",
    "mris_simulate_atrophy_params",
]
